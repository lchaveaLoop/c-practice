import tensorflow as tf
import os
import zipfile


# !wget --no-check-certificate \
#     "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/happy-or-sad.zip" \
#     -O "/tmp/happy-or-sad.zip"
URL='https://storage.googleapis.com/laurencemoroney-blog.appspot.com/happy-or-sad.zip'
NAME='happy-or-sad.zip'
PATH="E:/temp/"
train_data = tf.keras.utils.get_file(NAME,URL,PATH)

zip_ref = zipfile.ZipFile("E:/temp/happy-or-sad.zip", 'r')
zip_ref.extractall("/temp/h-or-s")
zip_ref.close()

# class myCallback(tf.keras.callbacks.Callback):
#   def on_epoch_end(self, epoch, logs):
#     if(logs.get('acc')>DESIRED_ACCURACY):
#       print("\nReached 99.9% accuracy so cancelling training!")
#       self.model.stop_training = True
#
# callbacks = myCallback()

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

from tensorflow.keras.optimizers import RMSprop

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['acc'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1/255)

train_generator=train_datagen.flow_from_directory(
    "/temp/h-or-s",
    target_size=(150,150),
    batch_size=10,
    class_mode='binary'
)

test_datagen=ImageDataGenerator(rescale=1.0/255)
validation_generator=test_datagen.flow_from_directory(
    "/temp/h-or-s",
    target_size=(150,150),
    batch_size=10,
    class_mode='binary'
)

# Expected output: 'Found 80 images belonging to 2 classes'

history = model.fit_generator(
    train_generator,
    steps_per_epoch=8,
    epochs=15,
    verbose=1
)