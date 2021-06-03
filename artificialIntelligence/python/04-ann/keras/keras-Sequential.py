from keras.models import Sequential
from keras.layers import Dense, Activation
#
#
model = Sequential([
    Dense(32, input_shape=(10,), activation="relu"),
    Dense(2, activation="softmax")
])
#
#
a = np.array([0,0,1,])
#
#
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
%matplotlib inline
#
#
a = np.array([1,0,0,1,1,0,0,1,0,1])
a.shape
#
#
img = np.expand_dims(plt.imread('nn.png'),0)
plt.imshow(img[0])
#
# In an ANN, the activation function of a neuron defines the output of that neuron given a set of inputs.
#Biologically inspired by activity in our brains, where different neurons fire, or are activated, by different stimuli.
from keras.models import Sequential
from keras.layers import Dense, Activation
#
#
# Keras sequential model
# The Sequential model is a linear stack of layers
#   Artificial Neural Networks are typically organized in layers.
#   Different types of layers include.
#
# Method 1 
model1 = Sequential([
    Dense(5, input_shape=(3,), activation="relu")
])
#
#
#Method 2
model2 = Sequential()  #create empy sequential model
model2.add(Dense(5, input_shape=(3,)))  #add first layer
model2.add(Activation("relu"))   #add second layer
#
#
# ------- Training ---------------------------------------------------
# Solving an optimization problem.
from keras.models import Sequential
from keras.layers import Dense, Activation
#
#
model = Sequential([
    Dense(5, input_shape=(3,), activation = "relu"),
    Dense(2, activation = "softmax")
])
#
#
# ------- Learning ---------------------------------------------------
# define what are the network parameters(metrics)
#
# Regularization 
import keras
import numpy as np
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
#
#
model = Sequential()
model.add(Dense(16, input_shape=(1,), activation="relu"))
model.add(Dense(32, activation="softmax"))
model.add(Dense(2, activation="sigmoid"))
#
#
model.compile(Adam(lr=.0001), loss="sparse_categorical_crossentropy", metrics = ["accuracy"])

# Loss Function 
model.loss = "sparse_categorical_entropy"
model.loss

# Learning Rate 
model.optimizer.lr = .0001
model.optimizer.lr
#
#
# scaled_train_samples and train_labels are numpy arrays to hold data
# define what is the batch size and other paramaters to set
scaled_train_samples = [0]
train_labels = [1]

model.fit(scaled_train_samples, train_labels, batch_size=10, epochs=20, shuffle=True, verbose=2)
#
#
# ------- Train, Validation and Test sets ---------------------------------------------------
scaled_train_samples = np.array([1,0,0,1,1,0,0,1,0,1])
train_labels = np.array([1,0,0,1,1,0,0,1,0,1])
model.fit(scaled_train_samples, train_labels, validation_split=.2, batch_size=10, epochs=20, shuffle=True, verbose=2)
# Another vay to create validation set data
#valid_set = [(sample, label), (sample, label), (sample, label), ... ,(sample, label)]
#model.fit(scaled_train_samples, train_labels, validation_data = valid_Set, batch_size=10, epochs=20, shuffle=True, verbose=2)
#
#
# ------- Predicting ---------------------------------------------------
# Passing our unlabeled test data to our model and then having our model predict on what it thinks about each sample in the test data.
scaled_test_samples = np.array([1,0,0,1,1,0,0,1,0,1])
predictions = model.predict(scaled_test_samples, batch_size=10, verbose=0)
#
for i in predictions:
    print(i)
# [<probability of 0>, <probability of 1>]
#
img2 = np.expand_dims(plt.imread('p.png'),0)
plt.imshow(img2[0])