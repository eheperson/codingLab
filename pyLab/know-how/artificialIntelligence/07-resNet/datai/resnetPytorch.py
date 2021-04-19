import torch
import torch.nn as nn
import torch.nn.functional as f 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import time
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
#    Helper Function Decleration
def readImg(p, n):
    """
    Read images from specific location
    p : path 
    n : num of images
    """
    array = np.zeros([n,64*32])
    #
    i = 0
    for img in os.listdir(p):
        imgPath = p + "\\" + img
        img = Image.open(imgPath, mode = "r")
        data = np.asarray(img, dtype="uint8")
        data = data.flatten()
        array[i, :] = data
        i += 1
    return array 
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
def conv1x1(inputPlane, outputPlane, stride = 1):
    """
        kernel size 1x1 convolutional layer
        inputPlane : input channel, channels of input image
        outputPlane : output channel, number of neuron
    """
    return nn.Conv2d(inputPlane, outputPlane, kernelSize = 1, stride = stride, bias=False)
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
def conv3x3(inputPlane, outputPlane, stride = 1):
    """
        kernel size 3x3 convolutional layer
        inputPlane : input channel, channels of input image
        outputPlane : output channel, number of neuron
    """
    return nn.Conv2d(inputPlane, outputPlane, kernelSize = 3, stride = stride, padding = 1, bias=False)
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
class residualLayer(nn.Module):
    """
        residul layer class,
        it contains shortcut property of residual network layer architecture
    """
    #
    expansion = 1
    #
    def __init__(self, inputPlanes, planes, stride = 1, downSample = None):
        """
        Residual Network Architecture Decleration
        Initializer
        """
        super(network, self).__init__()
        #
        self.conv1 = conv3x3(inputPlanes, planes, stride)    
        self.bn1 = nn.BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace = True)
        self.drop = nn.Dropout(0.9)  
        self.conv2 = conv3x3(planes, planes, stride)
        self.bn2 = nn.BatchNorm2d(planes)
        self.downSample = downSample
        self.stride = stride
    #
    def forward(self, x):
        """
        NN network layers connector function
        Forward Propagator
        """
        identity = x 
        #
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.drop(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.drop(out)
        #
        if self.downSample is not None :
            # to equalize "identity" and "out" dimensions
            identity = self.downSample(x)
        #
        out = out + identity # resnet shortcut
        #
        out = self.relu(out)
        return out
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
nClass = 2
#
class resNet(nn.Module):
    """
    resNet architecture class
    """
    def __init__(self, block, layersl nClass = nClass):
        super(resNet, self).__init__()
        #
        self.inPlanes
        self.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size = 3, stride = 2, padding = 1)
        self.layer1 = self._makeLayer(block, 64, layers[0], stride = 1)
        self.layer2 = self._makeLayer(block, 128, layers[1], stride = 2)
        self.layer3 = self._makeLayer(block, 256, layers[2], stride = 2)
        #
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = n.Linear(256*block.expansion, nClass)
        #
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode="fan_out", nonlinearity="relu")
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
    #
    def _makeLayer(self, block, planes, nBlock, stride=1):
        """
        Connector method,
        it connects resnet layers to each others
        """
        downsample = None 
        #
        if stride != 1 or self.inPlanes != planes*block.expansion :
            downSample = nn.Sequential(
                conv1x1(self.inplanes, planes*block.expansion, stride),
                nn.BatchNorm2d(planes*block.expansion))
            #
            layers = []
            layers.append(block(self.inPlanes, planes, stride, downSample))
            self.inPlanes = planse*block.expansion
            #
            for _ in range(1, nBlock):
                layers.append(block(self.inplanes, planes))
            #
            return nn.Sequential(*layers)
    #       
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x