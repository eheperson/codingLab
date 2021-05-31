# !/usr/local/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# sklearn library for regression
from sklearn.linear_model import LinearRegression
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\linear-regression-dataset.csv"
df = pd.read_csv(datapath,sep = ";")
#----------------------------------------------------------------------
# plot data
plt.scatter(df.experience,df.salary)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
#
#----------------------------------------------------------------------
linear_reg = LinearRegression()
#
x = df.experience.values.reshape(-1,1)
y = df.salary.values.reshape(-1,1)
#----------------------------------------------------------------------
# model training
linear_reg.fit(x,y)
#----------------------------------------------------------------------
# predictions
theta0 = linear_reg.predict([[0]])
print("theta0: ",theta0)
#
theta0_ = linear_reg.intercept_
print("theta0_: ",theta0_)   # y-axis interception point
#
theta1 = linear_reg.coef_
print("theta1: ",theta1)   # slope
####
####
#----------------------------------------------------------------------
# test cestion
salary_new = 1663 + 1138*11
print(salary_new)
#
print(linear_reg.predict([[11]]))
#
# visualize line
array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)  # experience
#
plt.scatter(x,y)
plt.show()
#
y_head = linear_reg.predict(array)  # salary
#
plt.plot(array, y_head,color = "red")
#
linear_reg.predict([[100]])










