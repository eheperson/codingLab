import numpy as np
import matplotlib.pyplot as plt
from math import e
#import matplotlib.animation as animation


number_of_data = 100

mu1 = np.array([2,3], dtype = 'float')
sigma1 = np.array([[1,1.5],[1.5,3]],)
# rng default  # For reproducibility
rnd_number_1 = np.random.multivariate_normal(mu1,sigma1,number_of_data)
print((rnd_number_1))


mu2 = [15,14]
sigma2 = np.array([[1,1.5],[1.5,3]], dtype = 'float')

rnd_number_2 = np.random.multivariate_normal(mu2,sigma2,number_of_data)
print(rnd_number_2)

fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
plt.scatter( rnd_number_1[:,0],rnd_number_1[:,1], c='r', marker='+')
plt.scatter( rnd_number_2[:,0],rnd_number_2[:,1], c='k', marker='o')
plt.show()

X0=np.ones((2*len(rnd_number_1),1), dtype = 'float')
print(X0)

X1=np.array(rnd_number_1[:,0]+rnd_number_2[:,0], dtype = 'float')

X2=np.array(rnd_number_1[:,1]+rnd_number_2[:,1], dtype = 'float')
print(X2)

Y_general =np.append(np.zeros((len(rnd_number_1),1),dtype = 'float') ,np.ones((len(rnd_number_1),1),dtype = 'float')).reshape(200,1)
print(Y_general)


X0_X1 = np.append( X0 ,   X1, axis =1  ).reshape(200,2)
print(X0_X1)
print('????????????????????')
X_general_unnormalized = np.append(X0_X1,X2,axis =1).reshape(200,3)
print(X_general_unnormalized  )


X0_max = np.max(X0)
#print(X0_max)

X1_max = np.max(X1)
#print(X1_max)
print("'''''''''''''''''''''''''''")
X1_norm = (X1 /50)
#print(X1_norm)
X2_max = np.max(X2)
#print(X2_max)

X2_norm = (X2 /50)
print(X2_norm)


X0_X1_norm = np.append( X0 ,   X1_norm, axis =1 ).reshape(200,2)
#print(X0_X1_norm)
X_general = np.append(X0_X1_norm,X2_norm, axis=1).reshape(200,3)
print(X_general)


training_number = len(X0)
print(training_number)


# # firstly, model function H(x) should be defined to train the network.
# # H(x) = 1/(1 + exp(teta_0*x0 + teta_1*x1 + teta_2*x2))

teta = np.random.uniform(low = -20,high = 100, size=(3,1))


error_func=np.ones((2*len(rnd_number_1),1), dtype = 'float')


learning_rate = 1

epsilon = 1e-3 * np.ones((len(X0) , 1 ) , dtype=float)

temp1 = 0
temp2 = 0
temp3 = 0

iteration = 0
#tetaxgenerel = np.array(teta[0]*X_general[:,0])
#tetetetteette = np.array(np.exp(-(teta[0]*X_general[:,0]+teta[1]*X_general[:,1]+teta[2]*X_general[:,2])))
print()
cccc=np.arange(0,200,1)
print(cccc)
#error_func=(-1/(training_number)*(Y_general*np.log(1/(1+np.exp(-(teta[0]*X_general[0]+teta[1]*X_general[1]+teta[2]*X_general[2]))))+...
                             #   (1-Y_general[0])*np.log(1-1/(1+np.exp(-(teta[0]*X_general[0]+teta[1]*X_general[1]+teta[2]*X_general[2]))))))

while (iteration < 500):
     #  ((sum(abs(error_func) > epsilon))!=0).any()
    iteration = iteration +1
    print(iteration)
    internal_error_func = error_func 

    for i in range(0,training_number,1):
        
        temp1 =(temp1 - learning_rate *(1/(1 + np.exp(-(teta[0]*X_general[i,0] + teta[1]*X_general[i,1] +teta[2]* X_general[i,2] ))) - Y_general[i])* X_general[i,0])   
        temp2 =(temp2 - learning_rate *(1/(1 + np.exp(-(teta[0]*X_general[i,0] + teta[1]*X_general[i,1] +teta[2]* X_general[i,2] ))) - Y_general[i])* X_general[i,1])
        temp3 =(temp3 - learning_rate *(1/(1 + np.exp(-(teta[0]*X_general[i,0] + teta[1]*X_general[i,1] +teta[2]* X_general[i,2] ))) - Y_general[i])* X_general[i,2])

    # print()
    # print(f"Temp1 is :{temp1}")
    # print(f"Temp2 is :{temp2}")
    # print(f"Temp3 is :{temp3}")
    # print(temp2)
    # print(temp3)
    # print()
    teta[0]=teta[0] + temp1/training_number
    # print(f"Teta [0] is :{teta[0]}")
    teta[1]=teta[1] + temp2/training_number
    # print(f"Teta[1] is :{teta[1]}")
    teta[2]=teta[2] + temp3/training_number
    # print(f"Teta[2] is :{teta[2]}")
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp1 = np.array([0],dtype = 'float')
    temp2 = np.array([0],dtype = 'float')
    temp3 = np.array([0],dtype = 'float')
    
    
    
    
    #error_func=(-1/(training_number)*(Y_general*np.log(1/(1+np.exp(-(teta[0]*X_general[:,0]+teta[1]*X_general[:,1]+teta[2]*X_general[:,2]))))+(1-Y_general[:,0])*np.log(1-1/(1+np.exp(-(teta[0]*X_general[:,0]+teta[1]*X_general[:,1]+teta[2]*X_general[:,2]))))))
    
        # if np.isnan(error_func[i:,0])==1:
        #         error_func[i:,0]=0
        # if np.isinf(error_func[i:,0])==1:
        #         error_func[i:,0]=10e3

        #error_func=np.ones((2*len(rnd_number_1),1), dtype = 'float')
    #for i in range(0,training_number,1):
        



    #print((sum(abs(error_func))))


print(teta[0])
print(teta[1])
print(teta[2])

#print((sum(abs(error_func))))

plt.figure()

plt.plot(cccc,1/(1+e**(-(teta[0]*X_general[:,0]+teta[1]*X_general[:,1]+teta[2]*X_general[:,2]))))
plt.plot(cccc,Y_general)
plt.show()







