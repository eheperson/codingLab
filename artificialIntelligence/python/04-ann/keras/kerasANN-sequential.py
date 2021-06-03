#

import keras as k

from keras import backend as b
from keras.models import Sequential
from keras.layers import Activation, Dropout
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
#
#
model = Sequential()

nHidden = 2
model.add(Dense(nHidden, input_shape=(748,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

nHidden = 2
model.add(Dense(nHidden, input_shape=(748,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

nHidden = 2
model.add(Dense(nHidden, input_shape=(748,)))
model.add(Activation('relu'))
#
#
model.summary()
#
#