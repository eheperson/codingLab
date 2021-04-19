# !/usr/local/bin/python
# -*- coding: utf-8 -*-  ``
#----------------------------------------------------------------------
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# sklearn library for classification
from sklearn.ensemble import RandomForestClassifier
#
# sklearn train test split
from sklearn.model_selection import train_test_split
#
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\classification-dataset.csv"
data = pd.read_csv(datapath)
#
data.drop(["id","Unnamed: 32"],axis=1,inplace = True)

#
data.diagnosis = [ 1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)
# normalization
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))
#
#  train test split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)
#
#  random forest
rf = RandomForestClassifier(n_estimators = 100,random_state = 1)
rf.fit(x_train,y_train)
print("Result : ",rf.score(x_test,y_test))





















