# -*- coding: utf-8 -*-
"""model2finalipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11r9tAaEznBqxG2_N4VUV2ytdrCpCW8Fh
"""

!pip install tensorflow
!pip install keras

!mkdir .kaggle

cd /root/.kaggle

from google.colab import files 
files.upload()

!kaggle datasets download -d paultimothymooney/chest-xray-pneumonia

!ls

!unzip chest-xray-pneumonia.zip

from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling2D
from keras.applications.vgg16 import  VGG16
from keras import optimizers


class VGG16Extended :

  def __init__(self):
    self.base_model = VGG16(weights = 'imagenet', include_top = False)
  
  def custom_global_average_pooling2D(self, extended_model):
    return GlobalAveragePooling2D()(extended_model)
  
  def add_dense_layer_nn(self, extended_model, **kwargs):
    return Dense(units = kwargs["units"], activation =  kwargs["activation"])(extended_model)
  
  def add_dropout_layer_nn(self, extended_model, units = 0.5):
    return Dropout(units)(extended_model)
  
  def __extend_vgg16_base(self):
     extended_model = self.base_model.output 
     extended_model = self.custom_global_average_pooling2D(extended_model)
     extended_model = self.add_dense_layer_nn(extended_model, units = 512, activation = "relu")
     extended_model = self.add_dropout_layer_nn(extended_model)
     extended_model = self.add_dense_layer_nn(extended_model, units = 64, activation = "relu")
     extended_model = self.add_dense_layer_nn(extended_model, units = 2, activation = 'sigmoid')

     return Model(inputs = self.base_model.input, outputs = extended_model)
    
  def compile(self):
    model = self.__extend_vgg16_base()
    model.compile(
        loss = "categorical_crossentropy",
        optimizer = optimizers.SGD(lr = 1e-4, momentum = 0.9),
        metrics = ['accuracy']
    )

    return model

import tensorflow as tf 

img_width, img_height = 250, 250
train_data = '/root/.kaggle/chest_xray/train'
test_data = '/root/.kaggle/chest_xray/test'
val_data = '/root/.kaggle/chest_xray/val'

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)
val_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    test_data,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
    val_data,
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical')
 
with tf.device("/device:GPU:0"):
   model = VGG16Extended().compile()
   history_buffer = model.fit_generator(
       train_generator,
       epochs = 20, shuffle = True, verbose = 1, validation_data = test_generator
   )

model.save('VGG16_extended_v1.h5')
print(history_buffer.history)

from google.colab import files
files.download('VGG16_extended_v1.h5')

"""# New Section"""