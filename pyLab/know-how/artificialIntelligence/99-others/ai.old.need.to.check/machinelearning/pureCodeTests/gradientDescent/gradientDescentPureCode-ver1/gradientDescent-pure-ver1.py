import numpy as np
import os
import matplotlib.pyplot as plt
import linal as l

#--------------------------------------------------------------
# Dataset Definition
X = l.linSpace(1, 11, 1)
T = [1.1,3.3,4.1,5.6,12,13,15.2,19.2,21,22.7]

# Number of training data
N = len(X)

#plt.figure()
#plt.plot(X,T)
#plt.show()

#--------------------------------------------------------------
# Dataset Preparation
X = l.one2two(X, axis=0)
T = l.one2two(T, axis=0)
Y = l.tensor(len(T),1)

print(T)
print(Y)

#--------------------------------------------------------------
# Neural Network Architecture
l1 = 1 # neurons in input layer
l2 = 1 #neurons in output layer

theta = l.tensor(l2,l1)
tmp = l.tensor(l2,l1)
temp = l.tensor(l2,l1)

a1 = l.tensor(l1,1)


z2 = l.tensor(l2,1)
a2 = l.tensor(l2,1)

print("---")
print(z2)
print("---")


#errorFcn = 1/(2*trainingNumber)*((theta[0,0 + theta[1,0]*x.T - y.T)**2)

alpha = float(0.0001)

epsilon = 10e-9

iteration = 0

iterMax = 100000

#-----------------------------------------------------------
## gradient descent algorithm

while iterMax > iteration: #(np.sum(np.absolute(errorFcn)) > epsilon) and (iterMax > iteration) :

    iteration = iteration + 1
    for i in range(N):
        a1 = [X[i][:]]
        z2 = l.matMul(theta, a1)
        Y[i][:] = z2[0]


        temp = l.matSum(temp, l.matSub(z2, [T[i][:]]))
    
        
    theta = l.matSub(tmp, l.matMulNum(temp, (alpha/(2*N))))

    if iteration%1000 == 0:
        print("Iteration  : ", iteration)
        print("Mean Error : ", l.errorFcn(Y,T))

print("Theta Matrix : ", theta)


l.plotter(T, "r", Y, "b")

