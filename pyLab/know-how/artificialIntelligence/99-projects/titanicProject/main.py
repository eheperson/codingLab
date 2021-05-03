#
import numpy as np
#
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
#
import os
import warnings
#
import titanic as t
#
#
#
warnings.filterwarnings('ignore')
#
plt.style.use('seaborn-whitegrid')
#print(plt.style.available)
#
t.seperator("Dataset Directory")
for dirName, _, fileName in os.walk("D:\Libraries\Datasets\Titanic"):
    for fileName in fileName:
        print(os.path.join(dirName, fileName))
print('*\n*')
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Load Dataset 
trainDataPath = r"D:\\Libraries\\Datasets\\Titanic\\titanic\\train.csv"
testDataPath = r"D:\\Libraries\\Datasets\\Titanic\titanic\\test.csv"
#
trainDF = pd.read_csv(trainDataPath)
testDF = pd.read_csv(testDataPath)
#
testPassengerDf = testDF["PassengerId"]
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Examine Dataset
t.seperator("Train Data Frame Columns")
print(trainDF.columns)
# #
#  Data Indexing : 
#         0 - 'PassengerId' : Unique identification for each passenger
#         1 - 'Survived'    : 1 is survived, 0 is dead
#         2 - 'Pclass'      : Passenger Class
#         3 - 'Name'        : Name of Passenge
#         4 - 'Sex'         : Gender of Passenger
#         5 - 'Age'         : Age of passenger
#         6 - 'SibSp'       : No of Siblins/shildren
#         7 - 'Parch'       : No of Parents/Children
#         8 - 'Ticket'      : Ticket No
#         9 - 'Fare'        : Price of the ticket
#         10 - 'Cabin'      : Cabin Type
#         11 - 'Embarked'   : port name embarked(foreach passenger)
# #
#
t.seperator("First 10 line of  training data")
print(trainDF.head(10))
#
t.seperator("Statistical informations of about numerical values of DataFrame")
print(trainDF.describe())
#
t.seperator("Information about train dataframe")
print(trainDF.info())
#
        # Float data  : 'Fare', 'Age'
        # int64 data  : 'Pclass', 'SibSp', 'Parch', 'PassengerId', 'Survived' 
        # Object data : 'Cabin', 'Embarked', 'Name', 'Sex', 'Ticket'
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Univariate Variable Analysis
    # 1- Categorical Variable
    # 2- Numerical Variable
#
# 1- Categorical Variable --------------------------------------------------#
#
#   > A categorical variable is a category or type. 
#     For example, hair color is a categorical value or hometown is a categorical variable. 
#     Species, treatment type, and gender are all categorical variables.
#
#   > Categorical Variables in titanic dataset : 
#           'Survived', 'Sex', 'Pclass', 'Embarked', 'Cabin', 'Name', 'Ticket', 'SibSp', 'Parch'
#
categoricalVars = ['Survived', 'Sex', 'Pclass', 'Embarked', 'Cabin', 'Name', 'Ticket', 'SibSp', 'Parch']
#
# uncomment below codes for graph output
# for c in categoricalVars:
#     t.barPlot(c, trainDF)
#
# 2- Numerical Variable ----------------------------------------------------#
#   > A numerical variable is a variable where the measurement or number has a numerical meaning. 
#     For example, total rainfall measured in inches is a numerical value, heart rate is a numerical value, 
#     number of cheeseburgers consumed in an hour is a numerical value.
#
#   > Numerical Variables in titanic dataset : 'Fare', 'PassengerId', 'Age'
#
numericalVArs = ['Fare', 'PassengerId', 'Age']
#
# uncomment below codes for graph output
# for n in numericalVArs:
#     t.plotHist(n, trainDF)
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Basic Data Analysis
#
# print(trainDF[["Pclass", "Survived"]])
#
# Gruping train dataframe
#
grouped = trainDF[["Pclass", "Survived"]].groupby(["Pclass"], as_index=False).mean()
#
t.seperator("'Pclass'-'Survived' relation (Mean Values)")
print(grouped.sort_values(by="Survived", ascending=False))
#
grouped = trainDF[["Sex", "Survived"]].groupby(["Sex"], as_index=False).mean()
#
t.seperator("'Sex'-'Survived' relation (Mean Values)")
print(grouped.sort_values(by="Survived", ascending=False))
#
grouped = trainDF[["SibSp", "Survived"]].groupby(["SibSp"], as_index=False).mean()
#
t.seperator("'SibSp'-'Survived' relation (Mean Values)")
print(grouped.sort_values(by="Survived", ascending=False))
#
grouped = trainDF[["Parch", "Survived"]].groupby(["Parch"], as_index=False).mean()
#
t.seperator("'Parch'-'Survived' relation (Mean Values)")
print(grouped.sort_values(by="Survived", ascending=False))
#
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Outlier Detection (Search for different outlier detection methods)
#
# Outlier :  Outliers are extreme values that deviate from other observations on data , 
#            they may indicate a variability in a measurement, experimental errors or a novelty. 
#            In other words, an outlier is an observation that diverges from an overall pattern on a sample.
#
# Why do I want to detect outliers?

    # An outlier may indicate bad data. For example, 
    # the data may have been coded incorrectly 
    # or an experiment may not have been run correctly.
    #
    # If it can be determined that an outlying point is 
    # in fact erroneous, then the outlying value should 
    # be deleted from the analysis (or corrected if possible).
#
    # In some cases, it may not be possible to determine 
    # if an outlying point is bad data. Outliers may be due 
    # to random variation or may indicate something scientifically interesting.
    #
    # In any event, we typically do not want to simply delete the outlying observation. 
    # However, if the data contains significant outliers, we may need to consider 
    # the use of robust statistical techniques.
#
# Detect Outliers 
outliers = trainDF.loc[t.detectOutliers(trainDF, ["Age", "SibSp", "Parch", "Fare"])]
#
t.seperator("Outliers for : 'Age', 'SibSp', 'Parch', 'Fare'")
print(outliers)
#
# Drop Outliers 
outliers = trainDF.drop(t.detectOutliers(trainDF, ["Age", "SibSp", "Parch", "Fare"]), axis=0).reset_index(drop = True)
#
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Missing Values 
#
#   In that step we will focus on 'NaN' value data in our dataset
#   And our purpose is to get rid of them
#
        # Steps : 
        #     1- Find missing values 
        #     2- Fill or Remove it
#
# !!! We have to find missing values for both test and train data frames
# Combining trainDF and testDF into a single data frame
trainDFsize = len(trainDF)
dataFrame = pd.concat([trainDF, testDF], axis=0).reset_index(drop=True)
#
# 1- Find missing value --------------------------------------------------#
missings = dataFrame.columns[dataFrame.isnull().any()]
#
t.seperator("Data has missing value : ")
print(missings)
#
t.seperator("Total numbers of missing values for each data row :")
# To see there is how many missing value in dataset 
print(dataFrame.isnull().sum())
#
# 2- Fill missing value --------------------------------------------------#
#
#   > "Embarked" has 2 missing and "Fare" has 1 missing
#   > We will fill "Embarked" and "Fare" in that step
#   > Filling "Age" is required more advanceinfo, so it will be filled in later steps
#   > "Survived" has 418 missin, all missings belogs to test dataset, we do not need fill it
#
t.seperator(" missing values in 'Embarked' data row")
embarkedMissings = dataFrame[dataFrame["Embarked"].isnull()]
print(embarkedMissings)
#
# we will try to fill missing "Embarked" values via comparing "Fear"
# we will compare "Fare" values of each "Survived" missing
# and we will try fill "Survived" according to "Fare"
# "Fare" values of missing data is 80.0
dataFrame.boxplot(column="Fare", by="Embarked")
plt.show()
# We could see from boxplot that :
# The passengers which their "Fear" values is 80 generally got on the ship from port C
# So we are going to fill missing "Emarked" value as C
dataFrame["Embarked"] = dataFrame["Embarked"].fillna("C")
#
# Next step is filling missing "Fare"  values via comaring "Pclass"
# The same procedure with filling "Embarked"
t.seperator(" missing values in 'Fare' data row")
fareMissings = dataFrame[dataFrame["Fare"].isnull()]
print(fareMissings)
#
# We could see in 'fareMissing' variable, 
# the tada which "Fare" is missing from it has Pclass=3
# So wecan observe all datas which have "Pclass=3" value : 
farePclass = dataFrame[dataFrame["Pclass"] == 3]
t.seperator(" 'Pclass = 3' values in data")
print (farePclass)
#
# calculating mean value of the value-cells which have
# Pclass=3 and their "Fare" values must be not missing
newFare = np.mean(farePclass = dataFrame[dataFrame["Pclass"] == 3]["Fare"])
# and write it to missing Fare : 
dataFrame["Fare"] = dataFrame["Fare"].fillna(newFare)
#
#
#
print('')
print('')
print('')
print('*\n*')
print('*\n*')
print('*\n*')