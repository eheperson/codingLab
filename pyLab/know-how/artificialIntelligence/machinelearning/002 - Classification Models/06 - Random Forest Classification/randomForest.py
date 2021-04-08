# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:54:05 2018

@author: kuzub

 - Kind of enseble learning
 
STEPS :
    1- Split data to train and test
    2- Select n sample from train data (subsample selection)
    3- Train that subsumple with decision tree classification
    4- return to step 1 and do it m times
    5- we will obtain m different decision tree model in final
    6- check the result of that m different decision tree
    7- max result will be output of classification
"""

import pandas as pd
import numpy as np
#%%  import data

data = pd.read_csv("data.csv")
data.drop(["id","Unnamed: 32"],axis=1,inplace = True)

# %%
data.diagnosis = [ 1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)
#%% normalization

x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

# %% train test split
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)

#%% decision tree
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

print("decision tree score: ", dt.score(x_test,y_test))

#%%  random forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 100,random_state = 1)
rf.fit(x_train,y_train)
print("random forest algo result: ",rf.score(x_test,y_test))



# %% Prediction
y_pred = rf.predict(x_test)
y_true = y_test
#%% confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true,y_pred)


# %% cm visualization
import seaborn as sns
import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize =(5,5))
sns.heatmap(cm,annot = True,linewidths=0.5,linecolor="red",fmt = ".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()































