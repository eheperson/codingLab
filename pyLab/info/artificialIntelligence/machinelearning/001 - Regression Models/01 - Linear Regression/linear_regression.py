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
#-------------- Plot Data Set  -----------------
#
plt.scatter(df.deneyim,df.maas)
plt.xlabel("deneyim")
plt.ylabel("maas")
plt.show()
#
#-------------- Linear Regression Model  -------------
#
linear_reg = LinearRegression()
#
x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)
#
#-------------- Fitting Data  -------------
#
linear_reg.fit(x,y)
#
#-------------- Model Coefficients -------------
b0_ = linear_reg.intercept_
print("b0_: ",b0_)   #Interception on y-axis
#
b1 = linear_reg.coef_
print("b1: ",b1)   # learning slope
#
# newSalary = b0 + b1*experience
#
#calculate from model coefficients 11 year experience salary
#
new_salary = b0 + b1*11
print(new_salary)
#
#-------------- Prediction   -------------
#
year4 = linear_reg.predict([[4]])
print("4 year experiencesalary: ",year4)
#
print(linear_reg.predict(11))
#
#-------------- Visualization  -------------
array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)  # experience
#
plt.scatter(x,y)
plt.show()
#
y_head = linear_reg.predict(array)  # salary
#
plt.plot(array, y_head,color = "red")
#
linear_reg.predict(100)
#
#
#####################################################
##-------------- R-Square Performance  -------------
#
from sklearn.metrics import r2_score
#
print("r_score : ", r2_score(y,y_head)












