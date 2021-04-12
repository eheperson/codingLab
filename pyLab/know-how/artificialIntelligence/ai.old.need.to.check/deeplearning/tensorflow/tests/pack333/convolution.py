# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:05:13 2020

@author: kuzub
"""
#
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.optimizers import SGD
from keras.utils import  np_utils
from keras.utils.vis_utils import plot_model
from keras import backend as k
#
from keras.datasets import mnist
#
import numpy as np 
#
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#
import cv2 as cv
#
#######################################################################################################
#importing dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#######################################################################################################
print("Initial shape or dimensions of x_train   :  " + str(x_train.shape))
print()
print("Number of samples in our training data   :  " + str(len(x_train)))
print("Number of labels in our training data    :  " + str(len(y_train)))
print("Number of samples in our test data       :  " + str(len(x_test)))
print("Number of labels in our test data        :  " + str(len(y_test)))
print()
print("Dimensions of x_train                    :  " + str(x_train[0].shape))
print("Labels in x_train                        :  " + str(y_train.shape))
print()
print("Dimensions of x_train                    :  " + str(x_test[0].shape))
print("Labels in x_train                        :  " + str(y_test.shape))
print()
#######################################################################################################
input_shape = x_train.shape
num_classes = len(y_train)
#######################################################################################################
# Take a look at some of images with opencv
for i in range(0,6):
    random_num = np.random.randint(0,len(x_train))
    img = x_train[random_num]
    window_name = "Random Sample #"+ str(i)
    cv.imshow(window_name, img)
    cv.waitKey(0)
#
cv.destroyAllWindows()
#######################################################################################################
# Take a look at some of images with matplotlib
plt.subplot(331)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))
#
plt.subplot(332)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))
#
plt.subplot(333)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))
#
plt.subplot(334)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))
#
plt.subplot(335)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))
#
plt.subplot(336)
random_num = np.random.randint(0,len(x_train))
plt.imshow(x_train[random_num], cmap=plt.get_cmap('gray'))
#
plt.show()
#######################################################################################################
# input image Shape for keras
img_rows = x_train[0].shape[0]
img_cols = x_train[1].shape[0]
#
# Getting our date in the right 'shape' needed for Keras
# we need to add a 4th dimension on our date thereby changinf our
# Our original image shape of (6000, 28, 28,1)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols,1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols,1)
#
#store the shape of single image
input_shape = (img_rows, img_cols, 1)
#
# change our image type to float32 data type
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
#
#Normalize our data by changing the range from (0 to 255) to (0 to 1)
x_train /= 255
x_test /= 255
#
print()
print('x_train_shape : ', x_train.shape)
print(x_train.shape[0], 'train_samples')
print(x_test.shape[0], 'test_samples')
#######################################################################################################
# One Hot encode our labesl
#
# One hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
#
# Lets Count The Number Columns in our hot encoded matrix
num_classes = y_test.shape[1]
num_pixels = x_train.shape[1]*x_train.shape[2]
#
#######################################################################################################
# Build Model
model = Sequential()
#
model.add(Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=input_shape))
#
model.add(Conv2D(64, (3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
#
model.add(Dropout(0.25))
#
model.add(Flatten())
model.add(Dense(128, activation='relu'))
#
model.add(Dropout(0.25))
#
model.add(Dense(num_classes, activation='softmax'))
#######################################################################################################
#compiling simply creates an object that stores our model we have just created
#We can specify our loss algorithm, optimizer and define our performance metrics. 
#Additional we can specify parameters for our optimizer such as learning rates and momentum
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(0.01),
              metrics = ['accuracy'])
#
print(model.summary())
#######################################################################################################

#following thelanguage from the most established python ML Library(Sklearn), we can fit our model with the follow code
batchSize = 32
epochNum = 5
history = model.fit(x=x_train, 
                    y=y_train, 
                    batch_size=batchSize, 
                    epochs=epochNum,
                    verbose=1,
                    validation_data=(x_test, y_test))
#######################################################################################################
#We can now simply evaluate our model's performance with this line of code
#loss_and_metrics = model.evaluate(x=x_test, x=y_test, batch_size=128)
score = model.evaluate(x_test,y_test, verbose = 0)
print()
print('Test Loss : ', score[0])
print("Test Accuracy : ", score[1])
print()
#######################################################################################################
# Plotting our loss charts

historyDict = history.history

lossValues = historyDict['loss']
validationLossValues = historyDict['val_loss']
epochs = range(1, len(lossValues) + 1)

line1 = plt.plot(epochs, validationLossValues, label="Validation/Test Loss")
line2 = plt.plot(epochs, lossValues, label="Training Loss")
plt.setp(line1, linewidth=2.0, marker='+', markersize=10.0)
plt.setp(line2, linewidth=2.0, marker='4', markersize=10.0)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.grid(True)
plt.legend()
plt.show()
#######################################################################################################
# Save Model
model.save("./test.h5")
print("Model Saved")
print()
#######################################################################################################
# load The Model
classifier = load_model("./test.h5")
#######################################################################################################
# Imput some of our test into our classifier

def draw_test(name, pred, input_im):
    BLACK = [0,0,0]
    expanded_image = cv.copyMakeBorder(input_im, 0, 0, 0, 0, imageL.shape[0], cv.BORDER_CONSTANT, values=BLACK)
    expanded_image = cv.cvtColor(expanded_image, cv.COLOR_BGR2GRAY)
    cv.putText(expanded_image, str(pred), (152,70), cv.FONT_HERSHEY_COMPLEX_SMALL,4, (0,255,0), 2)
    cv.imshow(name, expanded_image)

for i in range(0,10):
    rand = np.random.randint(0, len(x_test))
    input_im = x_test[rand]
    
    imageL = cv.resize(input_im, None, fx=4, f7=4, interpolation = cv.INTER_CUBIC)
    input_im = input_im.reshape(1,28,28,1)
    
    ## Get Prediction
    res = str(classifier.predict_classes(input_im,1 , verbose=0)[0])

    draw_test("Prediction", res, imageL)
    cv.waitKey(0)
#
cv.destroyAllWindows()        
#######################################################################################################
# Displaying Model Visually (Generating the diagram of the model architecture)
#
#Save our model diagrams to path
model_diagrams_path = './deeplearningcv/trainedModels/'
#
# Generate The Plot
plot_model(model,
           to_file=model_diagrams_path + 'model_plot_mnist.png',
           show_shapes = True,
           show_layer_names = True)
#
#Show the plot here
img = mpimg.imread(model_diagrams_path + 'model_plot.png')
plt.figure(figsize=(30,15))
implot = plt.imshow(img)
#######################################################################################################
# We can generate predictions by feeding our test data to the model.prediction function
classes = model.predict(x_test, batch_size=128)
#######################################################################################################
















































