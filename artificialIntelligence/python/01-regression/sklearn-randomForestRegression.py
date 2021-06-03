# !/usr/local/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# sklearn library for regression
from sklearn.ensemble import RandomForestRegressor
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\polynomial-regression-dataset.csv"
df = pd.read_csv(datapath,sep = ";")
#
#
x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)
# 
#
rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf.fit(x,y)
#
print("price at level 7.8 : ",rf.predict([[7.8]]))
#
x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = rf.predict(x_)
#
# visualize
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("price")
plt.show()
# 
