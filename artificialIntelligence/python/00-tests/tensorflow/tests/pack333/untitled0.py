# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:25:17 2020

@author: kuzub
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

datapath = ".."

data = pd.read_csv((datapath))

data.drop(["Unnamed : 32", "id"], axis=1, inplace=True)

data.diagnosis = [1 if each =="M" else 0 for each in data.diagnosis]

print(data.info)

y = data.diagnosis.values
x = data.drop(["diagnosis"], axis=1)

x = ( x - np.min(x)) / (np.max(x) - np.min(x)).values

#%% Train - Test Data Seperation
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 42)

xTrain = xTrain.T
xTest =  xTest.T
yTrain = yTrain.T
yTest = yTest.T

print()
print("xTrain datas : ", xTrain.shape)
print("xTest datas : ", xTest.shape)
print("yTrain datas : ", yTrain.shape)
print("yTest datas : ", yTest.shape)
print()

#%%  Parameter Initialization and Sigmoid Function

def initialize_weights_and_bias(dimension):
    
    w = np.full((dimension,1) , 0.01)
    b = 0.0
    return w, b

def sigmoid(z):
    
    y = 1 / (1 + np.exp(-z))
    return y

#%% Forward and Backward PAss Function

def fbPropagation(w, b, x, y):
    #Forward Propagation
    z = np.dot(w.T, xTrain) + b
    yTarget = sigmoid(z)
    loss = -y*np.log(yTarget) - 1(1 - y)*np.log(1 - yTarget)
    cost = (np.sum(loss)/x.shape[1])
    
    #Backward Propagation
    partialDerivativeW = (np.dot(x, ((yTarget - y).T))) / x.shape[1]
    partialDerivativeB = np.sum(yTarget - y)/x.shape[1]

    gradients = {"partial_derivative_weight" : partialDerivativeW, "partial_derivative_bias":partialDerivativeB}
    
    return cost, gradients

#%% Updating Weigtt and Bias Parameters

def update(w, b, x, y, lr, i):
    costList = []
    costListTemp = []
    index = []
    
    for i in range (i):
        # MAke Forward and Backward propagation then find cost and gradienst
        cost, gradients = fbPropagation(w, b, x, y)
        costList.append(cost)
        # Updating
        w = w - lr* gradients["partial_derivative_weight"]
        b = b - lr* gradients["partial_derivative_bias"]
        
        if i%10 ==0:
            costListTemp.append(cost)
            index.append(i)
            print("Cost After Iteration %i : , %f"%(i,cost))

    # Updated Weight and Bias Parameters
    parameters = {"weight":w, "bias":b}
    plt.plot(index,costListTemp)
    plt.xtixks(index, rotation='vertical')
    plt.xlabel("Number Of Iteration")
    plt.ylabel("Cost")
    plt.show()
    return parameters, gradients, costList

#%% Prediction Section
def predict(w, b, x): 
