# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 07:18:26 2020

@author: kuzub
"""

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import  matplotlib.pyplot as plt
from glob import glob

trainPath = "../../data/fruits-360/Training/"
testPath = "../../data/fruits-360/Test/"

img = load_img(trainPath + "Apple Braeburn/0_100.jpg")
# plt.imshow(img)
# plt.axis("off")
# plt.show()

x = img_to_array(img)
print(x.shape)

className = glob(trainPath + '/*')
numClass = len(className)
print("Number Of Classes  : ", numClass)
#%%  CNN MODEL

model = Sequential()

model.add(Conv2D(32,(3,3),input_shape=x.shape)) #filterNum:32 filterSize:3x3 inputShape:x.shape
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Conv2D(32,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation("relu"))

model.add(Dropout(0.5))
model.add(Dense(numClass))
model.add(Activation("softmax"))

#%% COMPILE MODEL
lossFuction = "categorical_crossentropy"
optMethod = "rmsprop"
metrics = ["accuracy"]

batch_size = 32

model.compile(loss=lossFuction, optimizer=optMethod, metrics=metrics)

#%% Data Augmentation

trainDataAugmented = ImageDataGenerator(rescale=1./255, shear_range=0.3, horizontal_flip=True, zoom_range=0.3)

testDataAugmented = ImageDataGenerator(rescale=1./255)

trainData = trainDataAugmented.flow_from_directory(trainPath, 
                                                   target_size = x.shape[:2],
                                                   color_mode="rgb",
                                                   class_mode="categorical")

testData = testDataAugmented.flow_from_directory(testPath, 
                                                   target_size = x.shape[:2],
                                                   color_mode="rgb",
                                                   class_mode="categorical")

#%% TRAIN MODEL

hist = model.fit_generator(generator=testData,
                    steps_per_epoch=1600//batch_size,
                    epochs=2,
                    validation_data=testData,
                    validation_steps=800//batch_size)

#%% MODEL SAVE

model.save_weights("deneme.h5")

#%% SAVE HISTORY

import json 

with open("deneme.json", "w") as f:
    json.dump(hist.history, f)
    
    
#%% LOAD FROM HISTORY

import codecs

with codecs.open("deneme.json", "r", encoding="utf-8") as f:
    modelHistory = json.loads(f.read())

#%% MODEL EVALUATION

print(modelHistory.keys())
plt.figure()
plt.plot(modelHistory["loss"], label="Train Loss")
plt.plot(modelHistory["val_loss"], label="Validation Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(modelHistory["accuracy"], label="Train Accuracy")
plt.plot(modelHistory["val_accuracy"], label="Validation Accuracy")
plt.legend()
plt.show()
