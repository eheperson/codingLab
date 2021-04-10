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
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\multiple-linear-regression-dataset.csv"
df = pd.read_csv(datapath,sep = ";")
#
x = df.iloc[:,[0,2]].values
y = df.salary.values.reshape(-1,1)
#
#  fitting data
multiple_linear_regression = LinearRegression()
multiple_linear_regression.fit(x,y)
#
print("b0: ", multiple_linear_regression.intercept_)
print("b1,b2: ",multiple_linear_regression.coef_)
#
# predict
multiple_linear_regression.predict(np.array([[10,35],[5,35]]))
#
#