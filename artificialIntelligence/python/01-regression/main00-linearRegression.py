# Install TensorFlow
# !pip install -q tensorflow-gpu==2.0.0-beta1
#
# --------------------------------------------------------
# Step 0 : Import required modules
# --------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
print("Tensorflow Version  :  ", tf.__version__)
#
# --------------------------------------------------------
# Step 1 : Load Data
# --------------------------------------------------------
# Get the data
#wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/moore.csv
print(" Data is Loaded...")
#
# Load in the data
data = pd.read_csv('moore.csv', header=None).values
X = data[:,0].reshape(-1, 1) # make it a 2-D array of size N x D where D = 1
Y = data[:,1]
#
# --------------------------------------------------------
# Step 2 : Examine & Explore Data
# --------------------------------------------------------
# Plot the data - it is exponential!
plt.scatter(X, Y)
#
# Since we want a linear model, let's take the log
Y = np.log(Y)
plt.scatter(X, Y)
# that's better
#
# Let's also center the X data so the values are not too large
# We could scale it too but then we'd have to reverse the transformation later
X = X - X.mean()
#
# --------------------------------------------------------
# Step 3 : Build the AI model
# --------------------------------------------------------
model = tf.keras.models.Sequential([
  tf.keras.layers.Input(shape=(1,)),
  tf.keras.layers.Dense(1)
])
#
model.compile(optimizer=tf.keras.optimizers.SGD(0.001, 0.9), loss='mse')
# model.compile(optimizer='adam', loss='mse')
#
# learning rate scheduler
def schedule(epoch, lr):
  if epoch >= 50:
    return 0.0001
  return 0.001
#
scheduler = tf.keras.callbacks.LearningRateScheduler(schedule)
#
# --------------------------------------------------------
# Step 4 : Train the model
# --------------------------------------------------------
r = model.fit(X, Y, epochs=200, callbacks=[scheduler])
#
# --------------------------------------------------------
# Step 5 : Evaluate and Plot the model metrics
# --------------------------------------------------------
# Plot the loss
plt.plot(r.history['loss'], label='loss')
#
# Get the slope of the line
# The slope of the line is related to the doubling rate of transistor count
print(model.layers) # Note: there is only 1 layer, the "Input" layer doesn't count
print(model.layers[0].get_weights())
#
# The slope of the line is:
a = model.layers[0].get_weights()[0][0,0]
#
print("Time to double:", np.log(2) / a)
#
# If you know the analytical solution
X = np.array(X).flatten()
Y = np.array(Y)
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator
print(a, b)
print("Time to double:", np.log(2) / a)
#
# --------------------------------------------------------
# Step 6 : Make Predictions
# --------------------------------------------------------
# Make sure the line fits our data
Yhat = model.predict(X).flatten()
plt.scatter(X, Y)
plt.plot(X, Yhat)
#
# Manual calculation
# Get the weights
w, b = model.layers[0].get_weights()
# Reshape X because we flattened it again earlier
X = X.reshape(-1, 1)
# (N x 1) x (1 x 1) + (1) --> (N x 1)
Yhat2 = (X.dot(w) + b).flatten()
# Don't use == for floating points
np.allclose(Yhat, Yhat2)