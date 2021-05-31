#
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Import required modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.neighbors import LocalOutlierFactor
from sklearn.decomposition import PCA
# warning library
import warnings
warnings.filterwarnings("ignore")
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Load and Examine Dataset
data = pd.read_csv(r"D:\GDrive\gitRepos\codingLab\pyLab\know-how\artificialIntelligence\tensorflow\tensorflow-2.x\projects\breastCancer\cancer.csv")
#
# remove some useless info columns from dataset
data.drop(['Unnamed: 32','id'], inplace = True, axis = 1)
#
# rename 'diagnosis' column as 'target'
data = data.rename(columns = {"diagnosis":"target"})
#
#Show the counts of observations in each categorical bin using bars.
print("*\n*")
sns.countplot(data["target"])
#
# get a Series containing counts of unique values. 
# How much 'Malignant' and 'Being'
print("*\n*")
print(data.target.value_counts())
#
# Convert categorical(string) data to numerical
print("*\n*")
data["target"] = [1 if i.strip() == "M" else 0 for i in data.target]
#
# Print length of the data 
print("*\n*")
print("length of the data : ",len(data))
#
# print first n rows of dataframe
# default : n=5
# data.head(n=10)
print("*\n*")
print(data.head(10))
#
# print data shape
print("*\n*")
print("Data shape ", data.shape)
#
# print a concise summary of a DataFrame.
print("*\n*")
data.info()
#
# calculating some statistical data like 
# percentile, mean and std of the numerical values
# (we may want standartize the data)
describe = data.describe()
print("*\n*")
print(describe)
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# EDA (Exploratory Data Science)
#
# Correlation Matrix
corrMatrix = data.corr()
sns.clustermap(corrMatrix, annot = True, fmt = ".2f")
print("*\n*")
plt.title("Correlation Between Features")
plt.show()
#
# Correlations higher than 0.75
# (There are some correlated features, We may want rwmove them )
# (Because they have no effect on training                     )
threshold = 0.75
filtre = np.abs(corrMatrix["target"]) > threshold
corrFeatures = corrMatrix.columns[filtre].tolist()
sns.clustermap(data[corrFeatures].corr(), annot = True, fmt = ".2f")
plt.title("Correlation Between Features w Corr Threshold 0.75")
plt.show()
#
# Box-Plot Draw
dataMelted = pd.melt(data, id_vars = "target",
                      var_name = "features",
                      value_name = "value")
# (We have to normalize or standardize our data )
# (to capture meaningfll info from box plot     )
# (That is required for actual dataset,         )
# (but im not sure if required always           )
plt.figure()
sns.boxplot(x = "features", y = "value", hue = "target", data = dataMelted)
plt.xticks(rotation = 90)
plt.show()
#
# pair plot 
# data is not standardized
# because of that,
# pairplot couldbe meaningless
# and we will only focus to 'corrFeatures'
sns.pairplot(data[corrFeatures], diag_kind = "kde", markers = "+", hue = "target")
plt.show()
# Skewness : search it!
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Outlier Detection
# ( We have to use true outlier detection method )
# ( which could handle skewness                  )
#       Density Based OutlierDetectionSystem : Local Outlier Factor(LOF)
#       will be used
#       - Compare local density of one point to
#         local density of its K-NN
y = data.target
x = data.drop(["target"],axis = 1)
columns = x.columns.tolist()
#
clf = LocalOutlierFactor()
yPred = clf.fit_predict(x)
xScore = clf.negative_outlier_factor_
#
outlierScore = pd.DataFrame()
outlierScore["score"] = xScore
#
# threshold
threshold = -2.5
filtre = outlierScore["score"] < threshold
outlierIndex = outlierScore[filtre].index.tolist()
#
plt.figure()
plt.scatter(x.iloc[outlierIndex, 0], x.iloc[outlierIndex, 1],color = "blue", s = 50, label = "Outliers")
plt.scatter(x.iloc[:,0], x.iloc[:,1], color = "k", s = 3, label = "Data Points")
#
radius = (xScore.max() - xScore)/(xScore.max() - xScore.min())
outlierScore["radius"] = radius
plt.scatter(x.iloc[:,0], x.iloc[:,1], s = 1000*radius, edgecolors = "r",facecolors = "none", label = "Outlier Scores")
plt.legend()
plt.show()
#
# drop outliers
x = x.drop(outlierIndex)
y = y.drop(outlierIndex).values
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Test-Train Split
test_size = 0.3
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = test_size, random_state = 42)
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Standarization
scaler = StandardScaler()
xTrain = scaler.fit_transform(xTrain)
XTest = scaler.transform(XTest)
#
xTrainDF = pd.DataFrame(xTrain, columns = columns)
xTrainDF_describe = xTrainDF.describe()
xTrainDF["target"] = yTrain
#
# box plot 
dataMelted = pd.melt(xTrainDF, id_vars = "target",
                      var_name = "features",
                      value_name = "value")
#
plt.figure()
sns.boxplot(x = "features", y = "value", hue = "target", data = dataMelted)
plt.xticks(rotation = 90)
plt.show()
#
# pair plot 
sns.pairplot(xTrainDF[corrFeatures], diag_kind = "kde", markers = "+",hue = "target")
plt.show()
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Basic KNN Method
#   > If we want to apply KNN we have to remove outliers from our dataset
#   > KNN has only 2 hyperparameter to tune (K-parameter, distance)
#   > Curse of dimensionality
#   > Feature scaling is required
#   > Inbalance data is a problem
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(xTrain, yTrain)
yPred = knn.predict(xTest)
cm = confusion_matrix(yTest, yPred)
acc = accuracy_score(yTest, yPred)
score = knn.score(xTest, yTest)
print("Score: ",score)
print("CM: ",cm)
print("Basic KNN Acc: ",acc)
#
# choose best parameters
def knnBestParams(xTrain, xTest, yTrain, yTest):
    #
    kRange = list(range(1,31))
    weightOptions = ["uniform","distance"]
    print()
    paramGrid = dict(n_neighbors = k_range, weights = weight_options)
    #
    knn = KNeighborsClassifier()
    grid = GridSearchCV(knn, param_grid, cv = 10, scoring = "accuracy")
    grid.fit(xTrain, yTrain)
    #
    print("Best training score: {} with parameters: {}".format(grid.best_score_, grid.best_params_))
    print()
    #
    knn = KNeighborsClassifier(**grid.best_params_)
    knn.fit(xTrain, yTrain)
    #
    yPredTest = knn.predict(xTest)
    yPredTrain = knn.predict(xTrain)
    #
    cmTest = confusion_matrix(yTest, yPredTest)
    cmTrain = confusion_matrix(yTrain, yPredTrain)
    #
    accTest = accuracy_score(yTest, yPredTest)
    accTrain = accuracy_score(yTrain, yPredTrain)
    print("Test Score: {}, Train Score: {}".format(accTest, accTrain))
    print()
    print("CM Test: ",cmTest)
    print("CM Train: ",cmTrain)
    #
    return grid
#   
grid = knnBestParams(xTrain, xTest, yTrain, yTest)
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Principial Component Analysis (PCA)
#
scaler = StandardScaler()
xScaled = scaler.fit_transform(x)

pca = PCA(n_components = 2)
pca.fit(xScaled)
xReducedPCA = pca.transform(xScaled)
pca = pd.DataFrame(xReducedPCA, columns = ["p1","p2"])
pca["target"] = y
sns.scatterplot(x = "p1", y = "p2", hue = "target", data = pca)
plt.title("PCA: p1 vs p2")
#
xTrainPCA, xTestPCA, yTrainPCA, yTestPCA = train_test_split(xReducedPCA, y, test_size = test_size, random_state = 42)
#
gridPCA = knnBestParams(xTrainPCA, xTestPCA, yTrainPCA, yTestPCA)
#
# visualize 
cmapLight = ListedColormap(['orange',  'cornflowerblue'])
cmapBold = ListedColormap(['darkorange', 'darkblue'])
@
h = .05 # step size in the mesh
X = xReducedPCA
xMin, xMax = X[:, 0].min() - 1, X[:, 0].max() + 1
yMin, yMax = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(xMin, xMax, h),
                     np.arange(yMin, yMax, h))
#
Z = gridPca.predict(np.c_[xx.ravel(), yy.ravel()])
#
# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
#
# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
            edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("%i-Class classification (k = %i, weights = '%s')"
          % (len(np.unique(y)),grid_pca.best_estimator_.n_neighbors, grid_pca.best_estimator_.weights))
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Neighborhood Component Analysis (NCA)
nca = NeighborhoodComponentsAnalysis(n_components = 2, random_state = 42)
nca.fit(xScaled, y)
X_reduced_nca = nca.transform(xScaled)
nca_data = pd.DataFrame(X_reduced_nca, columns = ["p1","p2"])
nca_data["target"] = y
sns.scatterplot(x = "p1",  y = "p2", hue = "target", data = nca_data)
plt.title("NCA: p1 vs p2")
#
xTrain_nca, xTest_nca, yTrain_nca, yTest_nca = train_test_split(X_reduced_nca, y, test_size = test_size, random_state = 42)
#
grid_nca = knnBestParams(xTrain_nca, xTest_nca, yTrain_nca, yTest_nca)
#
# visualize 
cmap_light = ListedColormap(['orange',  'cornflowerblue'])
cmap_bold = ListedColormap(['darkorange', 'darkblue'])
#
h = .2 # step size in the mesh
X = X_reduced_nca
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
#
Z = grid_nca.predict(np.c_[xx.ravel(), yy.ravel()])
#
# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
#
# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
            edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("%i-Class classification (k = %i, weights = '%s')"
          % (len(np.unique(y)),grid_nca.best_estimator_.n_neighbors, grid_nca.best_estimator_.weights))
#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
# Find wrongdecisions
knn = KNeighborsClassifier(**grid_nca.best_params_)
knn.fit(xTrain_nca,yTrain_nca)
y_pred_nca = knn.predict(xTest_nca)
accTest_nca = accuracy_score(y_pred_nca,yTest_nca)
knn.score(xTest_nca,yTest_nca)
#
test_data = pd.DataFrame()
test_data["xTest_nca_p1"] = xTest_nca[:,0]
test_data["xTest_nca_p2"] = xTest_nca[:,1]
test_data["y_pred_nca"] = y_pred_nca
test_data["yTest_nca"] = yTest_nca
#
plt.figure()
sns.scatterplot(x="xTest_nca_p1", y="xTest_nca_p2", hue="yTest_nca",data=test_data)
#
diff = np.where(y_pred_nca!=yTest_nca)[0]
plt.scatter(test_data.iloc[diff,0],test_data.iloc[diff,1],label = "Wrong Classified",alpha = 0.2,color = "red",s = 1000)