# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:45:40 2018

@author: kuzub

KNN : K Nearest Neighbors
    Steps :
        1- Pick the 'k' value
        2- Find the nearest k data points
        3- Calculate how many class between nearest neighbors there are
        4- Detect our test data in whichh class

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier

# %%
# data.csv
dataPath = "..."

data = pd.read_csv(dataPath)

# %% Clear Unused Data Features
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)

data.tail()
# malignant = M  kotu huylu tumor
# benign = B     iyi huylu tumor

# %%  Seperate Data 
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]

#%% scatter plot of the data
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha= 0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi",alpha= 0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

#%% make data more useful 
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)

#%% Normalize data
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

#%% Splist data to test and train
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=1)
# %% KNN MODEL

# n_neighbors = k
knn = KNeighborsClassifier(n_neighbors = 3) 

#%% TRain Model
knn.fit(x_train,y_train)

# model score
print(" {} nn score: {} ".format(3,knn.score(x_test,y_test)))

#%% Prediction
prediction = knn.predict(x_test)

# %% Calculating 'k' hyper parameter
score_list = []

for each in range(1,100):
    knn2 = KNeighborsClassifier(n_neighbors = each)
    knn2.fit(x_train,y_train)
    score_list.append(knn2.score(x_test,y_test))
    
plt.plot(range(1,100),score_list)
plt.xlabel("k values")
plt.ylabel("accuracy")
plt.show()


