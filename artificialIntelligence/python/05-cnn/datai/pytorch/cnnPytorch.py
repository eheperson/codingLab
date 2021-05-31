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
nClass = 2
class network(nn.Module):
    #
    def __init__(self):
        self.conv1 = nn.Conv2d(1, 10, 5)
        self.conv2 = nn.Conv2d(10,16,5)
        self.pool = nn.MaxPool2d(2,2)
        #
        self.fc1 = nn.Linear(16*13*5, 520)
        self.fc2 = nn.Linear(520, 130)
        self.fc3 = nn.Linear(130, nClass)
    #
    def forward(self, x):
        x = self.pool(f.relu((self.conv1(x))))
        x = self.pool(f.relu((self.conv2(x))))
        #
        x.view(-1, 16*13**5) # to flatten
        #
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = self.fc3(x)
        #
        return x
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #



# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #




# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #



# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
