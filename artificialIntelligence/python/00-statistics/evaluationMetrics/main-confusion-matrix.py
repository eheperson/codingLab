# !/usr/local/bin/python
# -*- coding: utf-8 -*-  ``
#----------------------------------------------------------------------
#   That evaluation matric is generally used for classification algorithms
#   CLASSIFICATION ALGORITHMS EVALUATION METRIC
#----------------------------------------------------------------------
#
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#
# sklearn library for classification
from sklearn.ensemble import RandomForestClassifier
#
# sklearn cofusion matrix import
from sklearn.metrics import confusion_matrix
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
#
# normalization
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))
#
# train test split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)
#
# Random Forest Classifier
rf = RandomForestClassifier(n_estimators = 100,random_state = 1)
rf.fit(x_train,y_train)
print("Random Forest Result : ",rf.score(x_test,y_test))
#
y_pred = rf.predict(x_test)
y_true = y_test
#
# Confusion Matrix
cm = confusion_matrix(y_true,y_pred)
#
# confuson matrix visualization
f, ax = plt.subplots(figsize =(5,5))
sns.heatmap(cm,annot = True,linewidths=0.5,linecolor="red",fmt = ".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()

















