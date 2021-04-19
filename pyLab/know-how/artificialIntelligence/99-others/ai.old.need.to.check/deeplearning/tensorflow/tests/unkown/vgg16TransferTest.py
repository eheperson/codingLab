# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 07:18:26 2020

@author: kuzub
"""

from keras.models import Sequential
from keras.layers import Dense

from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

from keras.applications.vgg16 import VGG16

import  matplotlib.pyplot as plt
from glob import glob

trainPath = "../../data/fruits-360/Training/"
testPath = "../../data/fruits-360/Test/"

img = load_img(trainPath + "Apple Braeburn/0_100.jpg")
# plt.imshow(img)
# plt.axis("off")
# plt.show()

x = img_to_array(img)
print("Input Image Shape           : " + str(x.shape))

className = glob(trainPath + '/*')
numClass = len(className)
print("Number Of Classes           : ", numClass , "\n\n\n")

#%% MODEL IMPORTING AND SUMMARY

vgg = VGG16()

print(vgg.summary())

print(type(vgg))

vgg_layer_list = vgg.layers
print(vgg_layer_list)

#%% MODEL BUILDING

model = Sequential()

for i in range(len(vgg_layer_list) - 1):
    model.add(vgg_layer_list[i])
    
print(model.summary())

for layers in model.layers:
    layers.trainable = False

model.add(Dense(numClass, activation="softmax"))

print(model.summary())

#%% COMPILE MODEL
lossFuction = "categorical_crossentropy"
optMethod = "rmsprop"
metrics = ["accuracy"]

batch_size = 32

model.compile(loss=lossFuction, optimizer=optMethod, metrics=metrics)

#%% Data Loading And Augmentation

trainData = ImageDataGenerator(rescale=1./255, 
                                        shear_range=0.3, 
                                        horizontal_flip=True, 
                                        zoom_range=0.3).flow_from_directory(trainPath,
                                                                            target_size = (224,224),
                                                                            color_mode="rgb",
                                                                            class_mode="categorical")

testData = ImageDataGenerator(rescale=1./255).flow_from_directory(testPath, 
                                                                           target_size = (224,224),
                                                                           color_mode="rgb",
                                                                           class_mode="categorical")
#%% TRAIN MODEL

hist = model.fit_generator(generator=testData,
                    steps_per_epoch=1600//batch_size,
                    epochs=1,
                    validation_data=testData,
                    validation_steps=800//batch_size)

#%% MODEL SAVE

model.save_weights("deneme2.h5")

#%% MODEL EVALUATION

print(hist.history.keys())
plt.figure()
plt.plot(hist.history["loss"], label="Train Loss")
plt.plot(hist.history["val_loss"], label="Validation Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(hist.history["accuracy"], label="Train Accuracy")
plt.plot(hist.history["val_accuracy"], label="Validation Accuracy")
plt.legend()
plt.show()

#%% SAVE HISTORY

import json 

with open("deneme2.json", "w") as f:
    json.dump(hist.history, f)
    
    
# #%% LOAD FROM HISTORY

# import codecs

# with codecs.open("deneme2.json", "r", encoding="utf-8") as f:
#     modelHistory = json.loads(f.read())


