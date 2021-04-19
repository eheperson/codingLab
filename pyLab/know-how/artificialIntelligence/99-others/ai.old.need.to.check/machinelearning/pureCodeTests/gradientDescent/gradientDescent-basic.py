import numpy as np
import os
import matplotlib.pyplot as plt

x = np.arange(1, 11, 1)

y = np.array([1.1,3.3,4.1,5.6,12,13,15.2,19.2,21,22.7])

plt.figure(1)
plt.plot(x,y)


#-----------------------------------------------------------

#firstly, model function H(x) should be define to train the network.
# H(x) = teta_0 + teta_1*x
theta = np.ones((2,1), dtype=float)
trainingNumber= x.size

#-----------------------------------------------------------

# then, cost function should be prepared in order to be appropriate form
# J(teta) = 1/2m*summation((h(x) -y)^2)

# firstly, initial values should be assigned.

errorFcn = 1/(2*trainingNumber)*((theta[0,0] + theta[1,0]*x.T - y.T)**2)

alpha = 0.0001

epsilon = 10e-9

iteration = 0

iterMax = 50000

#-----------------------------------------------------------
## gradient descent algorithm

print(y.shape)

while (np.sum(np.absolute(errorFcn)) > epsilon) and (iterMax > iteration) :

    iteration = iteration + 1
    
    for i in range(0,trainingNumber):

        temp1 = theta[0,0] - alpha*(1/trainingNumber)*(theta[0,0] + theta[1,0]*x[i] - y[i])
        temp2 = theta[1,0] - alpha*(1/trainingNumber*(theta[0,0] + theta[1,0]*x[i] - y[i]))*x[i]

        theta[0,0] = temp1
        theta[1,0] = temp2
        errorFcn[i] = 0.5*trainingNumber*((theta[0,0] + theta[1,0]*x[i] - y[i])**2)
        
 
    #print(errorFcn)
    #print("Error     : ", np.sum(np.absolute(errorFcn)))
    #print("Iteration : ", iteration)
    #os.system('cls' if os.name == 'nt' else 'clear')
    
plt.figure(2)    
plt.plot(x, y, 'r--', x, theta[0,0] + theta[1,0]*x, 'b--')
#plt.plot(x,theta[0,0] + theta[1,0]*x)
plt.show()
print(errorFcn)