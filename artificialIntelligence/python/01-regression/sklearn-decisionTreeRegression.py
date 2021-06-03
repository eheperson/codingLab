# !/usr/local/bin/python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# sklearn library for regression
from sklearn.tree import DecisionTreeRegressor
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\decision-tree-regression-dataset.csv"
df = pd.read_csv(datapath,sep = ";")
#
#

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#  decision tree regression
tree_reg = DecisionTreeRegressor()   # random sate = 0
tree_reg.fit(x,y)


tree_reg.predict([[5.5]])
x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = tree_reg.predict(x_)
# visualize
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color = "green")
plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()