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
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
#
from sklearn.linear_model import LogisticRegression
#
from sklearn.svm import SVC
#
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensembe import VotingClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
#
from sklearn.metrics import accuracy_score
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
# Missing Values - I
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
newFare = np.mean(dataFrame[dataFrame["Pclass"] == 3]["Fare"])
# and write it to missing Fare : 
dataFrame["Fare"] = dataFrame["Fare"].fillna(newFare)
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Visualization
#
# Correlation Matrix   --------------------------------------------------#
# between SibSp-Parch-Age-Fare-Survived
featureList = ['SibSp', 'Parch', 'Age', 'Fare', 'Survived']
sns.heatmap(dataFrame[featureList].corr(), annot=True, fmt = ".3f")
plt.show()
# We could observe that from correlation matrix :
#       'Fare' feature seems to have good correlation with 'Survived' feature (0.26) 
#
# Correlation Between SibSp-Survived  --------------------------------------------------#
g = sns.factorplot(x="SibSp", y="Survived", data=dataFrame, kind="bar", size=5)
g.set_ylabels("Survived Probability")
plt.show()
# Observations :
#     - Having a lot of SibSp have less chance to survive.
#     - if SibSp==0 or 1 or 2, passenger has more chance to survive
#     - We can consider a new feature describing these categories
#
# Correlation Between Parch-Survived  --------------------------------------------------#
g = sns.factorplot(x="Parch", y="Survived", data=dataFrame, kind="bar", size=5)
g.set_ylabels("Survived Probability")
plt.show()
# Observations :
#     - SibSp and Parch could be used for new feature extraction  with threshold:>3
#     - Small families have more chance to surveive
#
# Correlation Between Pclass-Survived  --------------------------------------------------#
g = sns.factorplot(x="Pclass", y="Survived", data=dataFrame, kind="bar", size=5)
g.set_ylabels("Survived Probability")
plt.show()
# Observations :
#     - Firs class passengers have more change to survive
#
# Correlation Between Age-Survived  --------------------------------------------------#
g = sns.FacetGrid(dataFrame, col='Survived')
g.map(sns.distplot, "Age", bins=25)
plt.show()
# Observations :
#     - We should know that, age distribution always will have a gaussian distribution because of its nature.
#     - Age <= 10 has a high survival rate
#     - Oldest passengers(80) survived
#     - Large number of 20 years old did not survive
#     - Most passengers are in 15-35 age range
#
# Relation Between Pclass-Age-Survived  --------------------------------------------------#
g = sns.FacetGrid(dataFrame, col='Survived', row='Pclass', size=2)
g.map(sns.histplot, "Age", bins=25)
g.add_legend()
plt.show()
# Observations :
#     - I do not know ho to interprate that graph.
#
# Relation Between Embarked-Sex-Pclass-Survived  --------------------------------------------------#
g = sns.FacetGrid(dataFrame, row='Embarked', size=2)
g.map(sns.pointplot, "Pclass", "Survived", "Sex")
g.add_legend()
plt.show()
# Observations :
#     - Female passengers have much better sruvival rate than males.
#     - Males have better survival rate in pclass 3 in C
#     - Embarked and Sex features could be used in training
#
# Relation Between Embarked-Sex-Fare-Survived  --------------------------------------------------#
g = sns.FacetGrid(dataFrame, row='Embarked', col="Survived", size=2.3)
g.map(sns.barplot,"Sex", "Fare")
g.add_legend()
plt.show()
# Observations :
#     - Passengers who pay higher fare have better survival.
#     - Fare can be used as categorical for training
#
# Relation Between Embarked-Sex-Pclass-Survived  --------------------------------------------------#
g = sns.FacetGrid(dataFrame, row='Embarked', size=2)
g.map(sns.pointplot, "Pclass", "Survived", "Sex")
g.add_legend()
plt.show()
# Observations :
#     - Female passengers have much better sruvival rate than males.
#     - Males have better survival rate in pclass 3 in C
#     - Embarked and Sex features could be used in training
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Missing Values - II (Age Feature)
#
# To see data don't have Age feature
dataFrame[dataFrame["Age"].isnull()]
#
# We have to predict and than fill that missing Age values.
# For that purpose, we have to examine other features and try
# to find a correlation to fill Age feature
#
# First trying to examine "Sex" feature and chec if we could find
# any relation to fill "Age"
g = sns.factorplot(x="Sex", y="Age", data=dataFrame, kind="box")
plt.show()
# Observation : Sex is not informative for age prediction,
#               because age distribution seems to be same.
#
# As a second trying, examine the "Pclass"
g = sns.factorplot(x="Sex", y="Age", hue="Pclass", data=dataFrame, kind="box")
plt.show()
# Observation : -First class passengers are older than second class and,
#                second class is older than 3rd class.
#               -Pclass could be usefull to fill 'Age'
#
# As a third examination, examine the "Sibsp" and "Parch" together
g = sns.factorplot(x="Parch", y="Age",  data=dataFrame, kind="box")
g = sns.factorplot(x="SibSp", y="Age",  data=dataFrame, kind="box")
plt.show()
# Observation : - Nothing for now
#
# Now, lets check he correlation between those features.
# Normally we cannot see the "Sex" feature on heatmap,
# BEcause the feature type is a string type.
# To be able to see, we need to convert it to numerical value.
dataFrame["Sex"] = [1 if i == "male" else 0 for i in dataFrame["Sex"]]
#
sns.heatmap(dataFrame[["Age", "Sex", "SibSp", "Parch", "Pclass"]].corr(), annot=True)
plt.show()
# Observation : Age is not correlated with Sex but it is correlated with Parch, SibSp and Pclass.
#
# After all, it is time to fill None values in 'Age' feature.
indexNanAge = list(dataFrame["Age"][dataFrame["Age"].isnull()].index)
for i in indexNanAge:
    agePrediction = dataFrame["Age"][(dataFrame["SibSp"] == dataFrame.iloc[i]["SibSp"]) & (dataFrame["Parch"] == dataFrame.iloc[i]["Parch"]) & (dataFrame["Pclass"] == dataFrame.iloc[i]["Pclass"])].median()
    #                                     ^
    # If any error in manual method above ^
    ageMedian = dataFrame["Age"].median()
    if not np.isnan(agePrediction):
        dataFrame["Age"].iloc[i] = agePrediction
    else :
        dataFrame["Age"].iloc[i] = ageMedian
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Feature Engineering
#
# Extracting new feature from "Name"  --------------------------------------------------#
#
dataFrame["Name"].head(10)
# The output of that cide will display passenger names with
# their titles. Names does not meaningfull for us but titles does.
# We could use titles to determine if any relationship exist between survival and titles.
#
names = dataFrame["Name"]
#
# 'McCharty, Mr. Timothy J' > 'McCharty, Mr.', 'Timoty J' > 'McCharty', ' Mr.', 'Timoty J' 
# Use .strip() to get ride of the gaps
# And wi will create new  feature as 'Title'
dataFrame["Title"] = [i.split('.')[0].split(',')[-1].strip() for i in names]
#
t.seperator(" First 10 rows of new feature 'Title' : ")
print(dataFrame["Title"].head(10))
#
# Histogram of titles
sns.countplot(x='Title', data=dataFrame)
plt.xticks(rotation = 60)
plt.show()
# Observation : We have to combine low count titles as 'Other'
## Replacing :
titlesReplace = ["Lady", "the Countess", "Col", "Don", "Dr", "Major", "Rev", "Sir", "Jonkheer", "Dona"]
dataFrame["Title"] = dataFrame["Title"].replace(titlesReplace, "Other")
#
# Now we need to convert srting values to numerical : 
#   Master, Miss
dataFrame["Title"] = [0 if i == "Master" else 1 if i == "Miss" or i == "Ms" or i == "Mlle" or i == "Mrs" else 2 if i =="Mr" else 3 for i in dataFrame["Title"]]
#
t.seperator(" First 10 rows of new feature 'Title' as numerical : ")
print(dataFrame["Title"].head(10))
#
# Now, we will ompare survival states according to "Title"
g = sns.factorplot(X="Title", y = "Survived", data=dataFrame, kind="bar")
g.set_xticklabels(["Master", "Mrs", "Mr", "Other"])
g.set_ylabels("Survival Probability")
plt.show()
# Observations : 
#   > We turn the useless "Name" feature to usefull "Title" feature.
#   > Passengers has Mrs title has more change of survival. 
# We could drop "Name" feature from data frame
dataFrame.drop(labels = ["Name"], axis = 1, inplace = True)
#
t.seperator(" First 10 rows of new data frame ('Name' feature is dropped) : ")
print(dataFrame["Title"].head(10))
#
# Converting Each value of "Title" to Feature
dataFrame = pd.get_dummies(dataFrame, columns = ["Title"])
t.seperator(" First 10 rows of new data frame ('title' feature is converted) : ")
dataFrame.head(10)
#
# Extracting new feature from "SibSp" and "Parch" --------------------------------------------------#
# we will name that new feature as "Fsize" : Family Size
dataFrame["Fsize"] = dataFrame["SibSp"] + dataFrame["Parch"] + 1
# +1 means that person
#
# Check if any relation between "Fsize" and "Survival"
g = sns.factorplot(X="Fsize", y = "Survived", data=dataFrame, kind="bar")
g.set_ylabels("Survival Probability")
plt.show()
#
# Next step is converting "Fsize" to categorical data
#   a treshold value picked as : 4.5
#   if family size < 4.5 = 1
#   if family size > 4.5 = 0
# creating new feature to store that categorical information
dataFrame["familySize"] = [1 if i < 5 else 0 for i in dataFrame["Fsize"]]
#
# histogram of "familySize" : 
#sns.countplot(x="familySize", data=dataFrame)
#plt.show()
#
# # Examine relation between survival and familySize
# g = sns.factorplot(X="familySize", y = "Survived", data=dataFrame, kind="bar")
# g.set_ylabels("Survival Probability")
# plt.show()
#   Observations : 
#       Small families have more change to survive than big families
#
# Converting Each value of "familySize" to Feature
dataFrame = pd.get_dummies(dataFrame, columns = ["familySize"])
#
# Extracting new feature from "Embarked" --------------------------------------------------#
#
# Counting how many kind "embarked" value
sns.countplot(x="familySize", data=dataFrame)
plt.show()
# Observations :
#   > There are 3 kind of embarked value : Q, S, C
# Now we will turn "Ebarked" to cathegorical
dataFrame = pd.get_dummies(dataFrame, columns = ["Embarked"])
#
# Extracting new feature from "Ticket" --------------------------------------------------#
#
tickets = []
for i in list(dataFrame.Ticket):
    if not i.isdigit():
        tickets.append(i.replace(".", "").replace("/", "").strip().split("")[0])
    else:
        ticketc.append("X")
dataFrame["Ticket"] = tickets
#
# Now we will turn "Ticket" to cathegorical
dataFrame = pd.get_dummies(dataFrame, columns = ["ticket"], prefix="T")
# mean of the  prefix="T" use "T" instead of "Ticket" when name new categorical features
#
# Extracting new feature from "Pclass" --------------------------------------------------#
#
# Counting how many kind "Pclass" value
sns.countplot(x="Pclass", data=dataFrame)
plt.show()
#
#There is nothing to do about "Pclass"
# But we will convert "Pclass" to categorical
dataFrame["Pclass"] = dataFrame["Pclass"].astype("category")
dataFrame = pd.get_dummies(dataFrame, columns = ["Pclass"])
#
# Extracting new feature from "Sex" --------------------------------------------------#
#
#There is nothing to do about "Sex"
# But we will convert "Sex" to categorical
dataFrame["Sex"] = dataFrame["Sex"].astype("category")
dataFrame = pd.get_dummies(dataFrame, columns = ["Sex"])
#
# Dropping useless feature for Machine Learning --------------------------------------------------#
#
dataFrame.drop(labels = ["PassengerID", "Cabin"], axis = 1, inplace = True)
#
#
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
# Machine Learning Model
#
# Create Train, Test and Validation data --------------------------------------------------#
#
testData = dataFrame[trainDFsize:]
testData.drop(labels = ["survived"], axis = 1, inplace = True)
#
trainData = dataFrame[:trainDFsize]
xTrain = trainData.drop(labels = ["survived"], axis = 1, inplace = True)
yTrain = trainData["survived"]
#
xTrain, xVal, yTrain, yVal = train_test_split(xTrain, yTrain, test_size=0.33, random_state=42)
# Val : Validation
#
t.seperator("train_test_split() output : ")
print("xTrain Size   : ", len(xTrain))
print("yTrain Size   : ", len(yTrain))
print("xVal Size     : ", len(xVal))
print("yVal Size     : ", len(yVal))
print("Test Size     : ", len(test))
#
# Simple Logistic Regression --------------------------------------------------#
#
logReg = LogisticRegression()
logReg.fit(xTrain, yTrain)
#
accLogRegTrain = round(score(xTrain, yTrain)*100, 2)
accLogRegTest =  round(score(xTest, yTest)*100, 2)
#
t.seperator(" Simple Logistic Regressin Accuracies  :  ")
print("Training Accuracy : %{}".format(accLogRegTrain))
print("Testing Accuracy : %{}".format(accLogRegTest))
#
# -----------------------------------------------------------------------------------------------------------------------#
## Hyperparameter Tuning -- Grid Search -- Cross Validation --------------------------------------------------#
# We will compare 5 ml classifier and evaluate mean accuracy of each 
# of them by stratified cross validation.
#   - Decision Tree, SVM, Random Forest, KNN, Logistic Regression
#
# 
random_state = 42
classifier = [DecisionTreeClassifier(random_state = random_state),
             SVC(random_state = random_state),
             RandomForestClassifier(random_state = random_state),
             LogisticRegression(random_state = random_state),
             KNeighborsClassifier()]
#
dt_param_grid = {"min_samples_split" : range(10,500,20),
                "max_depth": range(1,20,2)}
#
svc_param_grid = {"kernel" : ["rbf"],
                 "gamma": [0.001, 0.01, 0.1, 1],
                 "C": [1,10,50,100,200,300,1000]}
#
rf_param_grid = {"max_features": [1,3,10],
                "min_samples_split":[2,3,10],
                "min_samples_leaf":[1,3,10],
                "bootstrap":[False],
                "n_estimators":[100,300],
                "criterion":["gini"]}
#
logreg_param_grid = {"C":np.logspace(-3,3,7),
                    "penalty": ["l1","l2"]}
#
knn_param_grid = {"n_neighbors": np.linspace(1,19,10, dtype = int).tolist(),
                 "weights": ["uniform","distance"],
                 "metric":["euclidean","manhattan"]}
#
classifier_param = [dt_param_grid,
                   svc_param_grid,
                   rf_param_grid,
                   logreg_param_grid,
                   knn_param_grid]
#
#
cv_result = []
best_estimators = []
for i in range(len(classifier)):
    clf = GridSearchCV(classifier[i], param_grid=classifier_param[i], cv = StratifiedKFold(n_splits = 10), scoring = "accuracy", n_jobs = -1,verbose = 1)
    clf.fit(X_train,y_train)
    cv_result.append(clf.best_score_)
    best_estimators.append(clf.best_estimator_)
    print(cv_result[i])
#
#
cv_results = pd.DataFrame({"Cross Validation Means":cv_result, "ML Models":["DecisionTreeClassifier", "SVM","RandomForestClassifier",
             "LogisticRegression",
             "KNeighborsClassifier"]})

g = sns.barplot("Cross Validation Means", "ML Models", data = cv_results)
g.set_xlabel("Mean Accuracy")
g.set_title("Cross Validation Scores")
#
# 
# Ensemble Modeling
votingC = VotingClassifier(estimators = [("dt",best_estimators[0]),
                                        ("rfc",best_estimators[2]),
                                        ("lr",best_estimators[3])],
                                        voting = "soft", n_jobs = -1)
votingC = votingC.fit(X_train, y_train)
print(accuracy_score(votingC.predict(X_test),y_test))
#
#
# Prediction and SUbmission
test_survived = pd.Series(votingC.predict(test), name = "Survived").astype(int)
results = pd.concat([test_PassengerId, test_survived],axis = 1)
results.to_csv("titanic.csv", index = False)
#
#
print('')
print('')
print('')
print('*\n*')
print('*\n*')
print('*\n*')