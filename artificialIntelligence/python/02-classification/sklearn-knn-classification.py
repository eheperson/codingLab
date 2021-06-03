# !/usr/local/bin/python
# -*- coding: utf-8 -*-  ``
#----------------------------------------------------------------------
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
# sklearn library for classification
from sklearn.neighbors import KNeighborsClassifier
#
# sklearn train test split
from sklearn.model_selection import train_test_split
#
#----------------------------------------------------------------------
# import data
#   ! please enter the full path of your .csv file
# windows os : "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\lr-dataset.csv"
# linux os   : "D:/gitRepos/codingLab/pyLab/know-how/sklearn/datasets/lr-dataset.csv"
datapath = "D:\gitRepos\codingLab\pyLab\know-how\sklearn\datasets\classification-dataset.csv"
data = pd.read_csv(datapath)
#
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)
data.tail()
# malignant = M  kotu huylu tumor
# benign = B     iyi huylu tumor

# %%
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]
# scatter plot
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="ugly",alpha= 0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="beautiful",alpha= 0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()


data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)


# normalization 
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))


# train test split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=1)

# knn model

knn = KNeighborsClassifier(n_neighbors = 3) # n_neighbors = k
knn.fit(x_train,y_train)
prediction = knn.predict(x_test)
print(" {} nn score: {} ".format(3,knn.score(x_test,y_test)))


# find k value
score_list = []
for each in range(1,15):
    knn2 = KNeighborsClassifier(n_neighbors = each)
    knn2.fit(x_train,y_train)
    score_list.append(knn2.score(x_test,y_test))
    
plt.plot(range(1,15),score_list)
plt.xlabel("k values")
plt.ylabel("accuracy")
plt.show()

