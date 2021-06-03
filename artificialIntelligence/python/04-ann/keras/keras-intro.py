#
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
# --- Comosing Model in Keras ------------------------------------
# Sequential Composition
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

model.summary()

# Functional Composition
# The second way of composing modules is via the function API, where it is possimbe to define complex models.
# Keras functional API defines each layer as a function and provides operators to compose these functions into a larger computational graph
# https://keras.io/getting-started/functional-api-guide/