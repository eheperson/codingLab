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
from sklearn.linear_model import LinearRegression
#
#--------------- Import Data Set  -----------------
#
df = pd.read_csv("linear_regression_dataset.csv",sep = ";")
#
#-------------- Linear Regression Model  -------------
#
multiple_linear_regression = LinearRegression()
#
x = df.iloc[:,[0,2]].values
y = df.maas.values.reshape(-1,1)
#
linear_reg.fit(x,y)
#
#-------------- Fitting Data  -------------
#
multiple_linear_regression.fit(x,y)
#
#-------------- Model Coefficients -------------
#
b0 = multiple_linear_regression.intercept_
print("b0: ", b0)
#
print("b1,b2: ",multiple_linear_regression.coef_)
#
# newSalary = b0 + b1*experience + b2*old
#
#calculate from model coefficients 11 year experience and 27 years old salary
#
new_salary = b0 + b1*11 + b2*27
print(new_salary)
#-------------- Prediction   -------------
#
# 10 years experience and 35 years old
candidate1  = [10,35]
#
# 5 years experience and 35 years old
candidate1  = [5,35]
#
candidatesArr = np.array([candidate1, candidate2])
#
print(multiple_linear_regression.predict(candidatesArr))