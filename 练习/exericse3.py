import tensorflow as tf 
from tensorflow import keras 

minist=tf.keras.datasets.mnist
(train_images,train_labels),(test_images,test_labels)=minist.load_data()

train_images=train_images.reshape(60000,28,28,1)
train_images=train_images/255.0
test_images=test_images.reshape(10000,28,28,1)
test_images=test_images/255.0
model=tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)),#64代表64个过滤器每个过滤器的形状为3*3，relu会丢弃负值，input_shape中的1表示用1个字节计算颜色深度
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy')
model.fit(test_images,test_labels,epochs=10)