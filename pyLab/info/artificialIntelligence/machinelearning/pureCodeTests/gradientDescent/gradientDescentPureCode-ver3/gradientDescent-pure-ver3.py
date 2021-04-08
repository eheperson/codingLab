import numpy as np
import os
import matplotlib.pyplot as plt

import phNN as ph

#--------------------------------------------------------------
## Dataset Definition
X = ph.linSpace(1, 11, 1)
T = [1.1,3.3,4.1,5.6,12,13,15.2,19.2,21,22.7]

#--------------------------------------------------------------
## Neural Network Architecture Building

network = ph.phNN(X=X, T=T)

l1 = 1 # neurons in input layer
l2 = 1 #neurons in output layer
layers = [l1, l2]


network.construct(layers)

#--------------------------------------------------------------
# Plot Dataset

#plt.figure()
#plt.plot(X,T)
#plt.show()

#--------------------------------------------------------------
## Initialize Hyperparameters
alpha = float(0.0001)
epsilon = 10e-9
iteration = 0
iterMax = 100000

network.initParams(alpha=alpha, iterMax=iterMax, epsilon=epsilon)

#--------------------------------------------------------------
## Train Network
network.train()

#-----------------------------------------------------------
## gradient descent algorithm
network.plotOut("r", "b")

