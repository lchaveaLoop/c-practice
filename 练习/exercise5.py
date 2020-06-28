import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile

# URL='https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip'
# NAME='cats-and-dogs.zip'
# PATH='/temp/cats-and-dogs.zip'
# train_data=tf.keras.utils.get_file(NAME,URL,PATH)

local_zip = '/temp/cats-and-dogs.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()
print(len(os.listdir('/temp/PetImages/Cat/')))
print(len(os.listdir('/temp/PetImages/Dog/')))