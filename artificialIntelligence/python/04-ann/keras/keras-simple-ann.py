#
#
import keras as k
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler
#
#
# Creating Example Data to Processing -------------------------------------------------------------
train_labels = []
train_samples = []
#
# Example data :
#   - An experimental drug was tested on individuals from ages 13 to 65
#   - The trial had 2100 participants. Half were under 65 years old, half were over 65 years old.
#   - 95% of patients 65 or older experienced side effects.
#   - 95% of patients under 65 experienced no side effects.
#
for i in range (1000):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0)
    
    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(1)
    
for i in range(50):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(1)
    
    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(0)
#
# print raw data
for i in train_samples:
    print(i)
#
#
train_labels = np.array(train_labels)
train_samples = np.array(train_samples)
#
#
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform((train_samples).reshape(-1,1))
#
#
#print scaled data
for i in scaled_train_samples:
    print(i)
#
# Build a simple model -------------------------------------------------------------
model = Sequential([
    Dense(16,input_shape=(1,), activation="relu"),
    Dense(32, activation="relu"),
    Dense(2, activation="softmax")
])
#
model.summary()
#
# Train Model-------------------------------------------------------------
model.compile(Adam(lr=.0001), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
#
model.fit(scaled_train_samples, train_labels, validation_split=0.1, batch_size=10, epochs=20, shuffle=True, verbose=2)
#
# Build a Validation Data -------------------------------------------------------------
#   valid_set = [(sample, label), (sample, label), ... , (sample, label)] 
#
# Creating Test Data -------------------------------------------------------------
# Creating Test Data
test_labels = []
test_samples = []
#
for i in range(10):
    #the 5% of younger individuals who did experience side effects
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_labels.append(1)
    
    #the 5% of older individuals who did not experience side effects
    random_older = randint(64,100)
    test_samples.append(random_older)
    test_labels.append(0)

for i in range(200):
    #the 95% of younger individuals who did experience side effects
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_labels.append(1)
    
    #the 95% of older individuals who did not experience side effects
    random_older = randint(64,100)
    test_samples.append(random_older)
    test_labels.append(0)
#
test_labels = np.array(train_labels)
test_samples = np.array(train_samples)
#
scaler = MinMaxScaler(feature_range=(0,1))
scaled_test_samples = scaler.fit_transform((test_samples).reshape(-1,1))
#
predictions = model.predict(scaled_test_samples, batch_size=10, verbose=0)
#
for i in predictions:
    print(i)
#
rounded_predictions = model.predict_classes(scaled_test_samples, batch_size=10, verbose=0)
#
for i in rounded_predictions:
    print(i)
#
# Create Confusion Matrix  -------------------------------------------------------------
%matplotlib inline
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt
#
cm = confusion_matrix(test_labels, rounded_predictions)
#
def plotCm(cm,
          classes,
          normalize=False,
          title='confusion_matrix',
          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting 'normalize=True'.
    """
    
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes,rotation=45)
    plt.yticks(tick_marks, classes)
    
    if normalize:
        cm = cm.astype('float')/ cm.sum(axis=1)[:,np.newaxis]
        print("Normalized Confusion MAtrix")
    else:
        print("COnfusion Matrix, Without Normalization")
        
    print(cm)
    
    thresh = cm.max() / 2.
    
    for i,j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i,j],
                horizontalalignment = 'center',
                color='white' if cm[i, j] > thresh else "black")
        
    plt.tight_layout()
    plt.ylabel("True Label")
    plt.xlabel("Predicted Label")
#
cm_plot_labels = ['no_side_effects', 'half_side_effects']
#
plotCm(cm, cm_plot_labels, title='Confusion Matrix')
#
# Save And Load Model  -------------------------------------------------------------
#   The Save functions saves :
#       - The architecture of the model allowing to re-create the model
#       - The weights of the model.
#       - The training configurations(loss, optimizer)
#       - The state of the optimizer, allowing to resume training exactly where you are left off
#
#Saving Model
model.save('medical_trial_model.h5')

#Load Model
from keras.models import load_model
new_model = load_model('medical_trial_model.h5')
#
new_model.summary()
#
new_model.get_weights()
#
new_model.optimizer
#
# Model To .Json -------------------------------------------------------------
# if you only need tosave the architecture of a model, 
# and not its weights or its training configuration, 
# you can use the following function to save the architecture only.
#
# Save as Json
json_string = model.to_json()

# Save as Yaml
#yaml_strings = model.to_yaml()

json_string

# model reconstruction from json

from keras.models import model_from_json

model_architecture = model_from_json(json_string)

model_architecture.summary()

# Model Save Weights -------------------------------------------------------------
# If you  only need to save the weights of a model, you can use the following function save the weights only 
model.save_weights('model_weights.h5')
#
model2 = Sequential([
    Dense(16, input_shape=(1,), activation="relu"),
    Dense(32, activation="relu"),
    Dense(2, activation="softmax")
])
#
model2.load_weights('model_weights.h5')




