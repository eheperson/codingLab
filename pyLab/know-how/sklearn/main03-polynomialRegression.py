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
from sklearn.preprocessing import PolynomialFeatures
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\polynomial-regression-dataset.csv"
df = pd.read_csv(datapath,sep = ";")
#
#
y = df.max_vel.values.reshape(-1,1)
x = df.price.values.reshape(-1,1)
#
plt.scatter(x,y)
plt.ylabel("max_vel")
plt.xlabel("price")
plt.show()
#
# linear regression =  y = b0 + b1*x
# multiple linear regression   y = b0 + b1*x1 + b2*x2
# polynomial regression =  y = b0 + b1*x +b2*x^2 + b3*x^3 + ... + bn*x^n
#
polynomial_regression = PolynomialFeatures(degree = 2)
#
x_polynomial = polynomial_regression.fit_transform(x)
#
#
#  fit
linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial,y)
#
y_head2 = linear_regression2.predict(x_polynomial)
#
plt.plot(x,y_head2,color= "green",label = "poly")
plt.legend()
plt.show()
#
#





















