# -*- coding: utf-8 -*-
#
#
#-------------- Import Libraries  -------------------
#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
#--------------- Import Model     -------------------
#
from sklearn.tree import DecisionTreeRegressor
#
#--------------- Import Data Set  -------------------
#
df = pd.read_csv("decision tree regression dataset.csv",sep = ";",header = None)
#
#-------------- Plot Data Set  ----------------------
#
# No plotting
#
#--------------  Model  -------------
#
x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)
#
random_state = 0
#
tree_reg = DecisionTreeRegressor(rnadom_state=random_state)
#
#-------------- Fitting Data  -------------
#
tree_reg.fit(x,y)
#
#-------------- Model Coefficients -------------
#
# Nothing Here For That Model
#
#-------------- Prediction   -------------
#
tree_reg.predict(5.5)
#
x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = tree_reg.predict(x_)
#
#-------------- Visualization  -------------
#
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color = "green")
plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()




   # random sate = 0




# %% visualize
