# -*- coding: utf-8 -*-
# ## Random forest is a subdomain of enseble learning
#  Areas : body part classification, stock price prediction, movie suggestion(netflix)
#
#-------------- Import Libraries  -------------------
#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
#--------------- Import Model     -------------------
#
from sklearn.ensemble import RandomForestRegressor
#
#--------------- Import Data Set  -------------------
#
df = pd.read_csv("random forest regression dataset.csv",sep = ";",header = None)
#
#-------------- Plot Data Set  ----------------------
#
# No plotting
#
#-------------- Model  -------------
#
x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)
#
nEst = 100   # how much tree
randState = 42 # research it
#
rf = RandomForestRegressor(n_estimators = nEst, random_state = randState)
#
#-------------- Fitting Data  -------------
#
rf.fit(x,y)
#
#-------------- Model Coefficients -------------
#
# Nothing Here
#
#-------------- Prediction   -------------
#
print("7.8 seviyesinde fiyatın ne kadar olduğu: ",rf.predict(7.8))
#
x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = rf.predict(x_)
#
#-------------- Visualization  -------------
#
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()
#
####################################################
##-------------- R-Square Performance  -------------
#
from sklearn.metrics import r2_score
#
print("r_score : ", r2_score(y,y_head)


