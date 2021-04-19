#
# https://www.kaggle.com/ardamavi/sign-language-digits-dataset
# 
# install dataset from link given above 
# locate in in the same folder as that python script
# and rename it as : "dataset"
#
# reference tutorial : https://www.kaggle.com/kanncaa1/deep-learning-tutorial-for-beginners
####################################################################
import numpy as np
#
#
#-------- Initialize Parameters --------#
def dummy(param):
    dummyParam = param + 5
    return dummyParam
#
result = dummy(3)
#
def initWB(dims):
     w = np.full((dims,1), 0.01)
     b = 0.0
     return w, b
#
#--------  Forward Propagation --------#
def sigmoid(z):
    yHead = 1/(1 + np.exp(-z))
    return yHead 

def forwardP(w, b, X, T):
    z = np.dot(w.T, X) + b
    yHead = sigmoid(z)
    loss = -Y*np.log(yHead) - (1 - T)*np.log(1 - yHead)
    cost = (np.sum(loss))/X.shape[1]
    return cost
#
#--------  Backward Propagation --------#
def forwardBackwardP(w, b, X, T):
    #forward propagation
    z = np.dot(w.T, X) + b
    yHead = sigmoid(z)
    loss = -Y*np.log(yHead) - (1 - T)*np.log(1 - yHead)
    cost = (np.sum(loss))/X.shape[1]
    #backward propagation
    derivativeWeight = (np.dot(X, ((yHead - T).T)))/X.shape[1] # X.shape[1]  is for scaling
    derivativeBias = np.sum(yHead - T)/X.shape[1]               # X.shape[1]  is for scaling
    gradients = {"derivativeWeight": derivativeWeight,"derivativeBias": derivativeBias}
    return cost,gradients
#
#--------  Updating Parameters (Learning) --------#
def update(w, b, X, T, lr,iter):
    """
    w : weight
    b : bias
    X : input values (X)
    T : target values (T)
    lr : learning rate
    iter : number of iterations
    """
    costList = []
    costList2 = []
    index = []
    # updating(learning) parameters is iter times
    for i in range(iter):
        # make forward and backward propagation and find cost and gradients
        cost,gradients = forwardBackwardP(w,b,X,T)
        costList.append(cost)
        # lets update
        w = w - lr * gradients["derivative_weight"]
        b = b - lr * gradients["derivative_bias"]
        if i % 10 == 0:
            costList2.append(cost)
            index.append(i)
            print ("Cost after iteration %i: %f" %(i, cost))
    # we update(learn) parameters weights and bias
    parameters = {"weight": w,"bias": b}
    plt.plot(index,costList2)
    plt.xticks(index,rotation='vertical')
    plt.xlabel("Number of Iterarion")
    plt.ylabel("Cost")
    plt.show()
    return parameters, gradients, costList
#
#parameters, gradients, costList = update(w, b, X, T, lr = 0.009,iter = 200)
#
#--------  Prediction --------#
def predict(W, B, xTest):
    # xTest is a input for forward propagation
    z = sigmoid(np.dot(w.T,xTest)+b)
    yPrediction = np.zeros((1, xTest.shape[1]))
    # if z is bigger than 0.5, our prediction is sign one (y_head=1),
    # if z is smaller than 0.5, our prediction is sign zero (y_head=0),
    for i in range(z.shape[1]):
        if z[0,i]<= 0.5:
            yPrediction[0,i] = 0
        else:
            yPrediction[0,i] = 1

    return yPrediction
# predict(parameters["weight"],parameters["bias"],xTest)
#
#--------  Logistic Regression One Function  --------#
def logisticRegression(X, T, xTest, yTest, lr ,  iter):
    # initialize
    dimension =  X.shape[0]  # that is 4096
    w,b = initWB(dimension)
    # do not change learning rate
    parameters, gradients, costList = update(w, b, X, T, lr,iter)
    
    yPredictionTest = predict(parameters["weight"],parameters["bias"],xTest)
    yPredictionTrain = predict(parameters["weight"],parameters["bias"],X)

    # Print train/test Errors
    print("train accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_train - T)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_test - yTest)) * 100))
#
logistic_regression(X, T, xTest, yTest,lr = 0.01, iter = 150)
#
#