import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
#
#
# model = Sequential([laye1, layer2, layer3])
# or
# model.add(layer4)

model = Sequential([
    Dense(16,input_shape=(1,), activation="relu"),
    Dense(32, activation="relu"),
    Dense(2, activation="softmax")
])
#
#
model.summary()
#
#
model.compile(Adam(lr=.0001,), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
#
#
model.fit()