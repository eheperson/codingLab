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
Y = np.zeros([N,2])
#
#
X = np.transpose(X)
T = np.transpose(T)
Y = np.transpose(Y)
#------------------------------------------------------------------------------
## plot dataset
plt.figure(1)
plt.plot(X1[:nClass], X2[:nClass], 'rx', X1[nClass:nClass*2], X2[nClass:nClass*2], 'bo', X1[nClass*2:], X2[nClass*2:], 'g+')
plt.axis('equal')
#plt.show()
#
#------------------------------------------------------------------------------
## other parameters
error= np.ones([N]) 
totalError = np.sum(error)
#
#------------------------------------------------------------------------------
## neural network architecture
l1 = 3;      # input layer neuron number  (layer 1)
l2 = 10;      # hidden layer neuron number (layer 2)
l3  = 2;     # output layer neuron number (layer 3)
#
theta1 = np.zeros([l2,l1])
theta2 = np.zeros([l3,l2])
#
a1 = np.zeros([l1, 1])
a2 = np.zeros([l2, 1])
a3 = np.zeros([l3, 1])
#
z2 = np.zeros([l2, 1])
z3 = np.zeros([l3, 1])
#
d3 = np.zeros([l3, 1])
d2 = np.zeros([l2, 1])
#
D1 = np.zeros([l2, l1])
D2 = np.zeros([l3, l2])
#
theta1Tmp = np.zeros([l2, l1])
theta2Tmep = np.zeros([l3, l2])

#------------------------------------------------------------------------------
## backpropagation training algorithm

iteration = 0
epsilon = 0.1
alpha = 0.1
iterMax = 3000

while totalError > epsilon and iterMax>iteration: 
    
    iteration = iteration + 1
    
    D1 = np.zeros([l2, l1])
    D2 = np.zeros([l3, l2])

    for i in range(N):
        #forward pass
        a1 = X[:,i]
                
        z2 = np.matmul(theta1, a1)  
        a2 = 1/(1 + np.exp(-z2))
        
        z3 = np.matmul(theta2, a2)
        a3 = z3
        #a3 = 1/(1 + np.exp(-z3))  
        Y[:,i] = a3 


        #backward pass
        d3 = T[:,i] - Y[:,i]

        d2Temp1 = np.matmul(np.transpose(d3), theta2)
        d2Temp1 = d2Temp1.reshape(1,l2)

        d2Temp2 = np.matmul(d2Temp1, a2)

        d2 = d2Temp2*(1-a2)
        

        d3 = d3.reshape((l3,1))
        a2 = a2.reshape((l2,1))
        D2 = D2 + alpha*np.matmul(d3, np.transpose(a2))

        a1 = a1.reshape((l1,1))
        d2 = d2.reshape((l2,1))
        D1 = D1 + alpha*np.matmul(d2, np.transpose(a1))



        error[i] = np.sum(1/2*(T[:,i] - Y[:,i])**2)

    totalError = np.sum(error)
    if iteration%100 == 0:
        print("Iteration  : ", iteration)
        print("Mean Error : ", totalError/N)
    

    theta1 = theta1 + D1/N
    theta2 = theta2 + D2/N





#------------------------------------------------------------------------------
## plot
yPlot = np.zeros([330])

yPlot[:110] = 0
yPlot[110:220] = 1
yPlot[220:330] = 2

yModelPlot = 2*Y[0,:] + 1*Y[1,:]

plt.figure(2)
plt.plot(yModelPlot, 'r', yPlot,'b')


#plt.plot(yPlot)
#plt.figure(3)
#plt.plot(yModelPlot)





plt.show()