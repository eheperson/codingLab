# !/usr/local/bin/python
# -*- coding: utf-8 -*-  ``
#----------------------------------------------------------------------
#   That evaluation matric is generally used for regressionalgorithms
#   REGRESSION ALGORITHMS EVALUATION METRIC
#----------------------------------------------------------------------
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# sklearn library for regression
from sklearn.linear_model import LinearRegression
#
# sklearn rsquare evaluation import 
from sklearn.metrics import r2_score
#
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\linear-regression-dataset.csv"
df = pd.read_csv(datapath,sep = ";")
#
#
# plot data
plt.scatter(df.experience,df.salary)
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()
#
#
# linear regression model
linear_reg = LinearRegression()
#
x = df.experience.values.reshape(-1,1)
y = df.salary.values.reshape(-1,1)
#
linear_reg.fit(x,y)
#
y_head = linear_reg.predict(x)  # maas
#
plt.plot(x, y_head,color = "red")
#
print("r_square score: ", r2_score(y,y_head))



















