#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Import required libraries
from keras.layers import Dense, Dropout, Input, ReLU
from keras.models import Model, Sequential
from keras.optimizers import Adam
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Generator builder method for GANs
def generatorBuilder():
    # 'g' stands for generator
    g = Sequential()
    #
    g.add(Dense(units = 512, input_dim = 100))
    g.add(ReLU())
    #
    g.add(Dense(units = 512))
    g.add(ReLU())
    #
    g.add(Dense(units = 1024))
    g.add(ReLU())
    #
    g.add(Dense(units = 784, activation = "tanh"))
    #
    g.compile(loss = "binary_crossentropy",
                      optimizer = Adam(lr = 0.0001, beta_1 = 0.5))
    #
    return g
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Dsicriminator builder methot for GAN
def discriminatorBuilder():
    d = Sequential()
    #
    d.add(Dense(units=1024,input_dim = 784))
    #
    d.add(ReLU())
    d.add(Dropout(0.4))
    #
    d.add(Dense(units=512))
    d.add(ReLU())
    #
    d.add(Dropout(0.4))
    #
    d.add(Dense(units=256))
    d.add(ReLU())
    #
    d.add(Dense(units=1, activation = "sigmoid"))
    #
    d.compile(loss = "binary_crossentropy",
                          optimizer= Adam(lr = 0.0001, beta_1=0.5))
    #
    return d
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# GAN builder method
def GANbuilder(d, g):
    d.trainable = False
    ganInput = Input(shape=(100,))
    x = g(gan_input)
    ganOutput = d(x)
    gan = Model(inputs = ganInput, outputs = ganOutput)
    gan.compile(loss = "binary_crossentropy", optimizer="adam")
    return gan
    