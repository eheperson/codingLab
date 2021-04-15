# Install TensorFlow
# !pip install -q tensorflow-gpu==2.0.0-beta1
#
# --------------------------------------------------------
# Step 0 : Import required modules
# --------------------------------------------------------
from google.colab import files
import numpy as np
import tensorflow as tf
print("Tensorflow Version  :  ", tf.__version__)
#
# --------------------------------------------------------
# Step 1 : Load Data
# --------------------------------------------------------
from sklearn.datasets import load_breast_cancer
# Import train-test-split from sklearn
from sklearn.model_selection import train_test_split
# Import scaler from sklearn
from sklearn.preprocessing import StandardScaler
#
data = load_breast_cancer()
print("Breast Cancer Data is Loaded...")
#
# --------------------------------------------------------
# Step 2 : Examine & Explore Data
# --------------------------------------------------------
# check the type of 'data'
#print(type(data))
#
# note: it is a Bunch object
# this basically acts like a dictionary where you can treat the keys like attributes
#print(data.keys())
#
# 'data' (the attribute) means the input data
#print(data.data.shape)
# it has 569 samples, 30 features
#
# 'targets'
#print(data.target)
# note how the targets are just 0s and 1s
# normally, when you have K targets, they are labeled 0..K-1
#
# their meaning is not lost
#print(data.target_names)
#
# there are also 569 corresponding targets
#print(data.target.shape)
#
# you can also determine the meaning of each feature
#print(data.feature_names)
#
# --------------------------------------------------------
# Step 3 : Prepare The Data
# --------------------------------------------------------
# split the data into train and test sets
# this lets us simulate how our model will perform in the future
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.33)
N, D = X_train.shape
#
# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# --------------------------------------------------------
# Step 4 : Build the AI model
# --------------------------------------------------------
model = tf.keras.models.Sequential([
  tf.keras.layers.Input(shape=(D,)),
  tf.keras.layers.Dense(1, activation='sigmoid')
])
#
# Alternatively, you can do:
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Dense(1, input_shape=(D,), activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
# --------------------------------------------------------
# Step 5 : Train the model
# --------------------------------------------------------
r = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100)
#
# --------------------------------------------------------
# Step 6 : Evaluate the model metrics
# --------------------------------------------------------
# Evaluate the model - evaluate() returns loss and accuracy
print("Train score:", model.evaluate(X_train, y_train))
print("Test score:", model.evaluate(X_test, y_test))
#
# --------------------------------------------------------
# Step 7 : Plotting Section
# --------------------------------------------------------
# Plot what's returned by model.fit()
import matplotlib.pyplot as plt
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend()
#
# Plot the accuracy too
plt.plot(r.history['accuracy'], label='acc')
plt.plot(r.history['val_accuracy'], label='val_acc')
plt.legend()
#
# --------------------------------------------------------
# Step 8 : Make Predictions
# --------------------------------------------------------
P = model.predict(X_test)
print(P) # they are outputs of the sigmoid, interpreted as probabilities p(y = 1 | x)
#
# Round to get the actual predictions
# Note: has to be flattened since the targets are size (N,) while the predictions are size (N,1)
P = np.round(P).flatten()
print(P)
#
# Calculate the accuracy, compare it to evaluate() output
print("Manually calculated accuracy:", np.mean(P == y_test))
print("Evaluate output:", model.evaluate(X_test, y_test))
# --------------------------------------------------------
# Step 9 : Saving and Loading a Trained Model
# --------------------------------------------------------
# Save our trained model to a file:
#model.save('linearclassifier.h5')
#
# Load the model and confirm that it still works
# Note: there is a bug in Keras where load/save only works if you DON'T use the Input() layer explicitly
# So, make sure you define the model with ONLY Dense(1, input_shape=(D,))
# At least, until the bug is fixed
# https://github.com/keras-team/keras/issues/10417
#model = tf.keras.models.load_model('linearclassifier.h5')
#print(model.layers)
#model.evaluate(X_test, y_test)
#
# Download the file - requires Chrome (at this point)
#files.download('linearclassifier.h5')