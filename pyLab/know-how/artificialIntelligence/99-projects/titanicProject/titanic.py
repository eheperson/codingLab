#
#
import numpy as np
#
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
#
from collections import Counter
#
"""
Module for titanic project
"""

def barPlot(variable, dataFrame):
    """
    bar plotter method
    """
    # get specified feature from dataframe
    var = dataFrame[variable]
    # count number of feature (categorical variable)
    varValue = var.value_counts()
    #
    # visualization
    plt.figure(figsize=(9,3))
    plt.bar(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print("* * * * * * * * * * * * * * * * * * * * *")
    print("{} : \n {} ".format(variable, varValue))
    print("* * * * * * * * * * * * * * * * * * * * *")
#
#
def plotHist(variable, dataFrame):
    """
    histogram lotter method
    """
    # visualization
    plt.figure(figsize = (9,3))
    plt.hist(dataFrame[variable], bins=10)
    #
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} distribution with histogram". format(variable))
    #
    plt.show()
#
def seperator(t):
    print('')
    print('*\n*')
    print("* * * ", t, " : ")
    print("*")
#
def detectOutliers(dataFrame, features):
    """
    Outlier Detector Function
 
        Q1  : First Quartile
        Q3  : Third Quartile
        IQR : (Q3 - Q1)
        IQR x 1.5 = C (C : Outlier Detection Coeff)
        D < (Q1 - C) and D > (Q2 + C) are loutlier data.
    """
    outlierIndices = []
    #
    for f in features:
        # step-1 : find first quartile
        Q1 = np.percentile(dataFrame[f], 25)
        #step-2 : find secnd quartile
        Q3 = np.percentile(dataFrame[f], 75)
        #step-3 : calculate IQR
        IQR = Q3 - Q1
        #step-4 : calculate C
        C = IQR*1.5
        #step-5 : detect outliers with their indices 
        outlierMin = Q1 - C
        outlierMax = Q3 + C
        outlierList = dataFrame[(dataFrame[f]<outlierMin) | (dataFrame[f]>outlierMax)].index
        outlierIndices.extend(outlierList)
    #
    outlierIndices = Counter(outlierIndices)
    #
    # Remove passenger if more than 2 outliers detected
    multipleOutliers = list(i for i, v in outlierIndices.items() if v>2)
    #
    return multipleOutliers