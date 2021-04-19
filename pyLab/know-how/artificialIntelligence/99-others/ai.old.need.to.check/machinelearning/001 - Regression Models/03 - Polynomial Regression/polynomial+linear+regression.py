# -*- coding: utf-8 -*-
#
#
#-------------- Import Libraries  -----------------
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
#--------------- Import Model     -----------------
#
from sklearn.preprocessing import PolynomialFeatures
#
#--------------- Import Data Set  -----------------
#
df = pd.read_csv("polynomial regression.csv",sep = ";")
#
#-------------- Plot Data Set  -----------------
#
plt.scatter(df.araba_max_hiz,df.araba_fiyat)
plt.ylabel("araba_max_hiz")
plt.xlabel("araba_fiyat")
plt.show()
#
#-------------- Polynomial Regression Model  -------------
#
linear_regression = LinearRegression()
#
polynomial_regression = PolynomialFeatures(degree = 2)
#
y = df.araba_max_hiz.values.reshape(-1,1)
x = df.araba_fiyat.values.reshape(-1,1)
#
#-------------- Fitting Data  -------------
#
x_polynomial = polynomial_regression.fit_transform(x)
#
linear_regression.fit(x_polynomial,y)
#
#-------------- Model Coefficients -------------
#
# linear regression =  y = b0 + b1*x
# multiple linear regression   y = b0 + b1*x1 + b2*x2
# polynomial regression =  y = b0 + b1*x +b2*x^2 + b3*x^3 + ... + bn*x^n
#
#-------------- Prediction   -------------
#
y_head = linear_regression.predict(x_polynomial)
#
#-------------- Visualization  -------------
#
plt.plot(x,y_head,color= "green",label = "poly")
plt.legend()
plt.show()















