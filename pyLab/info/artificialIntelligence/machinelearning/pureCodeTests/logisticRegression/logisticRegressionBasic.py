import numpy as np
import os
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------
noOfData = 1000

mean1= [2,3]
cov1 = [[1,1.5], [1.5,3]] #diagonal covariance
x11, x12 = np.random.multivariate_normal(mean1, cov1, noOfData).T

mean2 = [5,4]
cov2 = [[1,1.5], [1.5,3]]
x21, x22 = np.random.multivariate_normal(mean2, cov2, noOfData).T

plt.figure(1)
plt.plot(x11, x12, 'rx', x21, x22, 'bo')
plt.axis('equal')

#------------------------------------------------------------------------------
X0 = np.ones(2*noOfData)
X1 = np.hstack((x11, x21))
X2 = np.hstack((x12, x22))

XgeneralUnnormalized = np.transpose(np.vstack((X0, X1, X2)))

norm1 = np.linalg.norm(X1)
X1normalized= X1/norm1

norm2 = np.linalg.norm(X2)
X2normalized= X2/norm2

Xgeneral = np.transpose(np.vstack((X0, X1normalized,X2normalized)))

Ygeneral = np.hstack((np.zeros(noOfData), np.ones(noOfData)))



#------------------------------------------------------------------------------
alpha = 0.01
epsilon = 1e-3

iteration = 1
iterMax = 5000

theta = np.zeros([3,1])

trainingNumber = X0.size
#------------------------------------------------------------------------------
##  Model
#  H(x) = 1/(1 + exp(theta0*x0 + theta1*x1 + theta2*x2))

z = theta[0,0]*Xgeneral[:,0] + theta[1,0]*Xgeneral[:,1] + theta[2,0]*Xgeneral[:,2]
h = 1/(1 + np.exp(-z))

zError = theta[0,0]*Xgeneral[:,0] + theta[1,0]*Xgeneral[:,1] + theta[2,0]*Xgeneral[:,2]
hError = 1/(1 + np.exp(-zError))
#------------------------------------------------------------------------------
##  Error Function
errorFcn = -(1/(trainingNumber))*(Ygeneral*np.log10(h) + (1 - Ygeneral)*np.log10(1 - h))


#------------------------------------------------------------------------------
##  Training Algorithm
while (np.sum(np.absolute(errorFcn)) > epsilon) and (iterMax > iteration) :
    
    iteration = iteration + 1
    
    for i in range(trainingNumber):
        z[i] = theta[0,0]*Xgeneral[i,0] + theta[1,0]*Xgeneral[i,1] + theta[2,0]*Xgeneral[i,2]
        h[i] = 1/(1 + np.exp(-z[i]))

        temp1 = theta[0,0] - alpha*(h[i] - Ygeneral[i])*Xgeneral[i,0]
        temp2 = theta[1,0] - alpha*(h[i] - Ygeneral[i])*Xgeneral[i,1]
        temp3 = theta[2,0] - alpha*(h[i] - Ygeneral[i])*Xgeneral[i,2]

        theta[0,0] = temp1
        theta[1,0] = temp2
        theta[2,0] = temp3
        
        zError[i] = theta[0,0]*Xgeneral[i,0]+ theta[1,0]*Xgeneral[i,1] + theta[2,0]*Xgeneral[i,2]
        hError[i] = 1/(1 + np.exp(-zError[i]))
        errorFcn[i] = -(1/(trainingNumber))*(Ygeneral[i]*np.log10(hError[i]) + (1 - Ygeneral[i])*np.log10(1 - hError[i]))
    
    if iteration%100 == 0:
        print("Iteration  : ", iteration)
        print("Mean Error : ", np.mean(errorFcn))

    #print(iteration)

hThetaX= 1/(1 + np.exp(-(theta[0,0]*Xgeneral[:,0] + theta[1,0]*Xgeneral[:,1] + theta[2,0]*Xgeneral[:,2])))
plt.figure(2)    
plt.plot(range(0,trainingNumber,1), hThetaX, 'rx', range(0,trainingNumber,1),Ygeneral, 'bx')
plt.show()