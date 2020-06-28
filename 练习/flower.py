import  os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# train_dandelion_dir='H:/flower/train_data/dandelion'
# train_roses__dir='H:/flower/train_data/roses'
# train_sunflowers_dir='H:/flower/train_data/sunflowers'
# train_tulips_dir='h:/flower/train_data/tulips'

train_gray_dir=os.path.join('H:/flower/train_gray')
path='H:/flower/train_gray/'

# Directory with our training dandelion pictures
train_dandelion_dir=os.path.join(path+'dandelion')
# Directory with our training roses pictures
train_roses__dir=os.path.join(path+'roses')
# Directory with our training sunflowers pictures
train_sunflowers_dir=os.path.join(path+'sunflowers')
# Directory with our training tulips pictures
train_tulips_dir=os.path.join(path+'tulips')

# len_dandelion=len(os.listdir(train_dandelion_dir))
# len_roses=len(os.listdir(train_roses__dir))
# len_sunflows=len(os.listdir(train_sunflowers_dir))
# len_tulips=len(os.listdir(train_tulips_dir))
# totla_lenth=len_tulips+len_roses+len_sunflows+len_dandelion

# print(totla_lenth)


#nueron network
model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(16,(3,3),activation='relu',input_shape=(300,300,1)),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(16,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dense(1,activation='softmax')
])

model.summary()

#compile the model
model.compile(
    loss=tf.nn.softmax_cross_entropy_with_logits,
    optimizer='adam',
    metrics=['acc']
)

#use imagedatagenerator to rescal all image by 1./255
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator=train_datagen.flow_from_directory(
    'H:/flower/train_data', #image dir
    target_size=(300,300),
    batch_size=120
)
history = model.fit_generator(
      train_generator,
      steps_per_epoch=20,
      epochs=15,
      verbose=2)