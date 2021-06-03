import numpy as np
import os
import matplotlib.pyplot as plt

import PHIlinal as phi

#--------------------------------------------------------------
## Dataset Definition
X = phi.linSpace(1, 11, 1)
T = [1.1,3.3,4.1,5.6,12,13,15.2,19.2,21,22.7]

#--------------------------------------------------------------
## Neural Network Architecture Building

l1 = 1 # neurons in input layer
l2 = 1 #neurons in output layer
layers = [l1, l2]
phi.construct(X, T, layers)

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

phi.initParams(alpha=alpha, maxIteration=iterMax, epsilon=epsilon)

#--------------------------------------------------------------
## Train Network
phi.train()

#-----------------------------------------------------------
## gradient descent algorithm
phi.plotOut("r", "b")

