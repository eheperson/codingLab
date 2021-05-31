# --------------------------------------------------------------------- # 
        # Abbreviations : 
        #     X : training input data
        #     T : training target data
        #     p : path
        #     n : number 
        #     s : size
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Import modules
import torch
import torch.nn as nn
import torch.nn.functional as f 
import torch.utils.data
import torch.optim as optim
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import time
#
import resnetPytorch as rn
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
#           Device confic GPU or CPU
print("*\n*")
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Device : ", device)
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
#   Read Train Negative 43390 image
# trainNegativeP : train_negative_images_path
trainNegativeP = r"D:\Libraries\Datasets\LSIFIR\Classification\Train\neg"
# trainNegativeN : train_negative_image_numbers
trainNegativeN = 43390
trainNegArr = rn.readImg(trainNegativeP, trainNegativeN)
#
xTrainNegTensor = torch.from_numpy(trainNegArr) 
print("*\n*")
print("xTrainNegTensor : ", xTrainNegTensor.size())
tTrainNegTensor = torch.zeros(42000, dtype=torch.long)
print("xTrainNegTensor : ", tTrainNegTensor.size())
#
# --------------------------------------------------------------------- #
#   Read Train Positive 1028 image
# trainPositiveP : train_positive_images_path
trainPositiveP = r"D:\Libraries\Datasets\LSIFIR\Classification\Train\pos"
# trainPositiveN : train_positive_image_numbers
trainPositiveN = 10208
trainPosArr = rn.readImg(trainPositiveP, trainPositiveN)
# 
xTrainPosTensor = torch.from_numpy(trainPosArr)
print("*\n*")
print("xTrainPosTensor : ", xTrainPosTensor.size())
tTrainPosTensor = torch.ones(10000, dtype=torch.long)
print("xTrainPosTensor : ", tTrainPosTensor.size())
#
# --------------------------------------------------------------------- #
# Concat Train Data
xTrain = torch.cat((xTrainNegTensor, xTrainPosTensor), 0)
tTrain = torch.cat((tTrainNegTensor, tTrainPosTensor), 0)
print("*\n*")
print("X Train : ", xTrain.size())
print("T Train : ", tTrain.size())
#
# --------------------------------------------------------------------- #
#   Read Test Negative 22050 image
# testNegativeP : test_negative_images_path
testNegativeP = r"D:\Libraries\Datasets\LSIFIR\Classification\Test\neg"
# testNegativeN : test_negative_image_numbers
testNegativeN = 22050
testNegArr = rn.readImg(testNegativeP, testNegativeN)
#
xTestNegTensor = torch.from_numpy(testNegArr[:18056, :])
print("*\n*")
print("xTestNegTensor : ", xTestNegTensor.size())
tTestNegTensor = torch.zeros(18056, dtype=torch.long)
print("tTestNegTensor : ", tTestNegTensor.size())
#
# --------------------------------------------------------------------- #
#   Read Test Positive 5944 image
# testPositiveP : test_positive_images_path
testPositiveP = r"D:\Libraries\Datasets\LSIFIR\Classification\Test\pos"
# testPositiveN : test_positive_image_numbers
testPositiveN = 5944
testPosArr = rn.readImg(testPositiveP, testPositiveN)
#
xTestPosTensor = torch.from_numpy(testPosArr)
print("*\n*")
print("xTestPosTensor : ", xTestPosTensor.size())
tTestPosTensor = torch.ones(testPositiveN, dtype=torch.long)
print("tTestPosTensor : ", tTestPosTensor.size())
#
# --------------------------------------------------------------------- #
# Concat Test Data
xTest = torch.cat((xTestNegTensor, xTestPosTensor), 0)
tTest = torch.cat((tTestNegTensor, tTestPosTensor), 0)
print("*\n*")
print("X Test : ", xTest.size())
print("T Test : ", tTest.size())
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Visualization 
plt.imshow(xTrain[45001,:].reshape(64,32), cmap='gray') # 45002 ve 1001
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
nClass = 2
# Hyper Parameters Settings 
nEpochs = 100
sBatch = 2000
lr = 0.0001
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Prepare Dataset
train = torch.utils.data.TensorDataset(xTrain, tTrain)
trainLoader = torch.utils.data.DataLoader(train, batch_size=sBatch, shuffle = True)
#
test = torch.utils.data.TensorDataset(xTest, tTest)
testLoader = torch.utils.data.DataLoader(test, batch_size=sBatch, shuffle = False)
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Build NN ARchitecture
model = rn.resNet(rn.residualLayer,[2,2,3])
# model = rn.resNet(rn.residualLayer,[2,2,3]).to(device)
#
# Loss and Optimizer Definition
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Train Section
start = time.time()
#
trainAcc = []
losses = []
testAcc = []
totalStep = len(trainLoader)
#
useGPU = False
#
for epoch in range(nEpochs):
    for i, data in enumerate(trainLoader):
        inputs = inputs.view(sBatch, 1, 64, 32)
        inputs = inputs.float()
        #
        # if useGPU=True
        if useGPU :
            if torch.cuda.is_available():
                inputs, labels = inputs.to(device), labels.to(device)
        #
        # output
        outputs = model(images)
        #
        # loss
        loss = criterion(outputs, labels)
        #
        # backward propagation and optimization
        optimizer.zero_grad()
        loss.backward()
        # update weights 
        optimizer.step()
        #
        if i%2 == 0:
            print("Epoch : {} {}/{}".format(epoch, i, totalStep))
    #
    # test via "test data"
    correct = 0
    total = 0
    with torch.no_grad(): 
        # close propagation, 
        # train is ended, 
        # it is time to test
        for data in testLoader:
            images, labels = data
            images = images.view(sBatch, 1, 64, 32)
            images = imagesl.float()
            #
            # if useGPU=True
            if useGPU :
                if torch.cuda.is_available():
                    images, labels = images.to(device), labels.to(device)
            #
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += label.size(0) 
            correct += (predicted == labels).sum().item()
    #
    acc1 = 100*correct/total
    print("Accuracy Test : ", acc1)
    testAcc.append(acc1)
    #
    # test via "train data"
    correct = 0
    total = 0
    with torch.no_grad(): 
        # close propagation, 
        # train is ended, 
        # it is time to test
        for data in trainLoader:
            images, labels = data
            images = images.view(sBatch, 1, 64, 32)
            images = imagesl.float()
            #
            # if useGPU=True
            if useGPU :
                if torch.cuda.is_available():
                    images, labels = images.to(device), labels.to(device)
            #
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += label.size(0) 
            correct += (predicted == labels).sum().item()
    #
    acc2 = 100*correct/total
    print("Accuracy Train : ", acc2)
    trainAcc.append(acc2)
#
print("*\n*")
print("Train is done !")
#
end = time.time()
processTime = (end - start)/60
print("Process Time : ", processTime)
#
losses.append(loss.item() )