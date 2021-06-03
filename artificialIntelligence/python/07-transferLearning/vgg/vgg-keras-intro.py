#
import numpy as np
import keras as k
import itertools
import matplotlib.pyplot as plt 
%matplotlib inline

from keras import backend as b
from keras.models import Sequential
from keras.layers import Activation, InputLayer
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *

from sklearn.metrics import confusion_matrix
#
# ---- Data Preprocessing ----------------------------------------------------------
trainDataPath = 'cats-and-dogs/train'
testDataPath = 'cats-and-dogs/test'
validDataPath = 'cats-and-dogs/valid'

trainBatches= ImageDataGenerator().flow_from_directory(trainDataPath,
                                                       target_size = (224, 224),
                                                       classes = ['dog', 'cat'],
                                                       batch_size = 10)

validBatches = ImageDataGenerator().flow_from_directory(validDataPath,
                                                        target_size = (224, 224),
                                                        classes = ['dog', 'cat'], 
                                                        batch_size = 4)

testBatches = ImageDataGenerator().flow_from_directory(testDataPath,
                                                       target_size=(224,224),
                                                       classes = ['dog', 'cat'],
                                                       batch_size = 10)
#
#plots  images with labels within jupyter-notebook
def plots(ims, figsize=(12,6), rows = 1, interp = False, titles = None):
    if type(ims[0]) is np.ndarray : 
        ims = np.array(ims).astype(np.uint8)
        if (ims.shape[-1] != 3) : 
            ims = ims.transpose((0, 2, 3, 1))
    f = plt.figure(figsize = figsize)
    cols = len(ims)//rows if len(ims)%2 == 0 else len(ims)//rows + 1
    for i in range(len(ims)):
        sp = f.add_subplot(rows, cols, i+1)
        sp.axis('Off')
        if titles is not None : 
            sp.set_title(titles[i], fontsize = 16)
        plt.imshow(ims[i], interpolation = None if interp else 'none')
#
imgs, labels = next(trainBatches)
#
plots(imgs, titles = labels)
# that will give one_hot encoding
#
# ---- Build Fine-Tuned VGG16 Model  ----------------------------------------------------------
vgg16 = k.applications.vgg16.VGG16()
#
vgg16.summary()
#
type(vgg16)
#
model = Sequential()
model.add(vgg16.layers[0])
for layer in vgg16.layers:
    model.add(layer)
#
model.summary()
#
model.layers.pop()
#
model.summary()
#
for layer in model.layers:
    layer.trainable = False
#
model.add(Dense(2, activation='softmax'))
#
model.summary()
#
# ---- Train The Model  ----------------------------------------------------------
model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])
#
model.fit_generator(trainBatches, 
                    steps_per_epoch=4,
                    validation_data=validBatches,
                    validation_steps = 4,
                    epochs = 5,
                    verbose = 2)
#
# ---- Predictions  ----------------------------------------------------------
testImgs, testLabels = next(testBatches)
plots(testImgs, titles=testLabels)
#
testLabels = testLabels[:,0]
testLabels
#
predictions = model.predict_generator(testBatches, steps=1, verbose=0)
#
#
# (confusion matrix code will be added)





