
import tensorflow as tf
import os
from tensorflow.keras import Model
from tensorflow.keras.layers import Conv2D,MaxPool2D,Flatten,Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.inception_v3 import InceptionV3

#用get_file获取inceptionV3权重文件,不过有墙在并没有什么用
# url='https://storage.googleapis.com/mledu-datasets/' \
#     'inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
# name=url.split('/')[-1]
# print(name)
# save='H:/code/'
# origen=tf.keras.utils.get_file(name,url,save)


# train_path='H:/coco-animals/train/'
train_path='H:/UCMerced_LandUse/Images/testing/'
train_dir=os.path.join(train_path)
# test_path='H:/coco-animals/val'
test_path='H:/UCMerced_LandUse/Images/testing/'
test_dir=os.path.join(test_path)

TARGET_SIZE=175
weight_file='H:/code/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

#实例化加载的模型
pre_trained_model = InceptionV3(
    input_shape=(TARGET_SIZE,TARGET_SIZE,3),
    include_top=False,
    weights=None
)

pre_trained_model.load_weights(weight_file)

#遍历加载的模型，并锁定,使其不会再参与到训练中
for layer in pre_trained_model.layers:
    layer.trainable = False

pre_trained_model.summary()

last_layer=pre_trained_model.get_layer('mixed7')
last_output=last_layer.output
x=Flatten()(last_output)
x=Dense(1024,activation='relu')(x)
# x=tf.keras.layers.Dropout(0.8)(x)
x=Dense(15,activation='softmax')(x)
model = Model( pre_trained_model.input,x)
model.compile(
    loss='categorical_crossentropy',
    # loss=tf.keras.losses.CategoricalCrossentropy(),
    optimizer='adam',
    metrics=['accuracy']
)



train_datagen = ImageDataGenerator(rescale=1/255,
                                   rotation_range=60,#随机旋转角度
                                   width_shift_range=0.3,#shift表示位移,随机移动
                                   height_shift_range=0.3,
                                   shear_range=0.4,#倾斜
                                   zoom_range=0.3,#缩放
                                   horizontal_flip=True#水平翻转
                                   )

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(TARGET_SIZE, TARGET_SIZE),
        batch_size=20,
        color_mode='rgb',
        class_mode='categorical')

test_datagen=ImageDataGenerator(rescale=1/255.0)

test_generator=test_datagen.flow_from_directory(
    test_dir,
    target_size=(TARGET_SIZE,TARGET_SIZE),
    color_mode='rgb',
    class_mode='categorical',
    batch_size=20
)

# model.compile(loss=tf.keras.losses.CategoricalCrossentropy(),optimizer='adam',metrics=['accuracy'])

history = model.fit_generator(
      train_generator,
      validation_data=test_generator,
      steps_per_epoch=15,
      epochs=100,
      verbose=2)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False
plt.rcParams["font.sans-serif"]=["SimHei"]

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(loss))

plt.figure()
plt.plot(epochs,acc, 'r', label='训练集正确率')
plt.plot(epochs, val_acc, 'b', label='验证集正确率')
plt.title('训练集与验证集正确率波动情况')

plt.figure()
plt.plot(epochs, loss, 'r', label='训练集损失函数')
plt.plot(epochs, val_loss, 'b', label='验证集损失函数')
plt.title('训练集与验证集损失函数波动情况')

plt.legend()



plt.show()

# tf.saved_model()