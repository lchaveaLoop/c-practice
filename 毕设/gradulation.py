import tensorflow as tf
import os
from tensorflow.keras.layers import Conv2D,MaxPool2D,Flatten,Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#读取图像文件
# train_path='H:/UCMerced_LandUse/Images/training_gray'
train_path='H:/UCMerced_LandUse/Images/training/'
train_dir=os.path.join(train_path)
validation_path='H:/UCMerced_LandUse/Images/testing/'
validation_dir=os.path.join(validation_path)

#带有图像增强的生成器
train_datagen=ImageDataGenerator(rescale=1/255.0,
                                 rotation_range=40,
                                 width_shift_range=0.2,
                                 height_shift_range=0.2,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip=True)

train_generator=train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    class_mode='categorical',
    batch_size=100
)

validation_datagen=ImageDataGenerator(rescale=1/255.0)

validation_genarator=validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    class_mode='categorical'
    # batch_size=1
)

#CNN
model=tf.keras.Sequential([
    Conv2D(16,(3,3),input_shape=(150,150,3),activation='relu'),
    MaxPool2D(2,2),
    Conv2D(32,(3,3),activation='relu'),
    MaxPool2D(2,2),
    Conv2D(32,(3,3),activation='relu'),
    Flatten(),
    Dense(512,activation='relu'),
    Dense(15,activation='softmax')
])

#不带图像增强的生成器
# train_datagen = ImageDataGenerator(rescale=1/255.0)
#
# train_generator = train_datagen.flow_from_directory(
#         train_dir,
#         target_size=(150, 150),
#         batch_size=15,
#         class_mode='categorical')
#
# validation_datagen=ImageDataGenerator(rescale=1/255.0)
#
# validation_generator=validation_datagen.flow_from_directory(
#     validation_dir,
#     target_size=(150, 150),
#     batch_size=15,
#     class_mode='categorical',
#     )

model.compile(loss=tf.keras.losses.CategoricalCrossentropy(),optimizer='adam',metrics=['accuracy'])

history = model.fit_generator(
      train_generator,
      validation_data=validation_genarator,
      steps_per_epoch=2,
      epochs=100,
      verbose=2
)

import matplotlib.pyplot as plt
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend(loc=0)
plt.figure()


plt.show()