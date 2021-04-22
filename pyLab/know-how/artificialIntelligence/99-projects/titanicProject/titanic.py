#
#
import numpy as np
#
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
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
