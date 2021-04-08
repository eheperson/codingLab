import numpy as np
import math as m
import matplotlib.pyplot as plt

"""
x = np.arange(1, 11, 1)

y = np.array([1.1,3.3,4.1,5.6,12,13,15.2,19.2,21,22.7])

plot1 = plt.figure()
plt.plot(x,y)

plt.show(block=False)

plot2 = plt.figure(2)
plt.plot(x,y)

plt.show(block=False)


"""
#-----------------------------------
#-----------------------------------
"""
noOfData = 1000

mean1= [2,3]
cov1 = [[1,1.5], [1.5,3]] #diagonal covariance
x11, x12 = np.random.multivariate_normal(mean1, cov1, noOfData).T

mean2 = [5,4]
cov2 = [[1,1.5], [1.5,3]]
x21, x22 = np.random.multivariate_normal(mean2, cov2, noOfData).T

plt.plot(x11, x12, 'rx', x21, x22, 'bo')
plt.axis('equal')
#plt.show()

X0 = np.ones([2*x11.size,1])
print(len(X0))
z = [x11;x21]

np.concatenate((a, b.T), axis=1)
"""
#-----------------------------------
#-----------------------------------
"""
x1 = np.ones(1000)
x2 = np.ones(1000)*2
x3 = np.ones(1000)*3

X = np.stack((x1,x2,x3), axis=-1)

np.savetxt("e.txt",X)

y = X[:,1:]
np.savetxt("y.txt",y)

H = 3;      # hidden neuron number
K = 2;      # output
I = 3;      # input

W = np.zeros([H,I])

#print(W)

a = np.ones([3,3])*2
b = np.ones([3,3])*3

print(np.multiply(a[1, :],b))

"""
"""
a = np.ones([2,3])*2
b = np.ones([3,4])*3
c = np.ones([4,5])*4
d = np.ones([5,1])*5



e = np.matmul(a,b)
f = np.matmul(e,c)
g = np.matmul(f,d)

print(g)
"""

import numpy as np
import matplotlib.pyplot as plt
#
#------------------------------------------------------------------------------
## load dataset
dataFile = open("class3_tr.csv", "rb")
dataset = np.loadtxt(dataFile, delimiter=",", skiprows=0)
#
#------------------------------------------------------------------------------
## defining dataset
N = dataset[:,1].size
nClass = N/3
nClass =int(nClass)
#
X0 = np.ones(N);       # bias
#
X1 = dataset[:,0]
X2 = dataset[:,1]
#
XUnnormalized = np.stack((X0, X1, X2), axis=-1)
#
norm1 = np.linalg.norm(X1)
X1normalized= X1/norm1
#
norm2 = np.linalg.norm(X2)
X2normalized= X2/norm2
#
X = np.transpose(np.vstack((X0, X1normalized, X2normalized)))
#
T = dataset[:,2:]
Y = np.zeros([N,])
#
#
print(T)