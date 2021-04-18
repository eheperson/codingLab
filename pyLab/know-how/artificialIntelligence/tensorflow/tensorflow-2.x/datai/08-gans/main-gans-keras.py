#
#
#   Autoencoders : 
#       - A kind of unsupervised learning methods
#       - Keras reference > https://blog.keras.io/building-autoencoders-in-keras.html 
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
# Load and examine dataset
(xTrain, tTrain), (xTest, tTest) = mnist.load_data()
xTrain = (xTrain.astype(np.float32)-127.5)/127.5
#
print(xTrain.shape)
#
xTrain = xTrain.reshape(xTrain.shape[0],xTrain.shape[1]*xTrain.shape[2])
print(xTrain.shape)
#
#plt.imshow(xTest[12])
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Load and examine dataset