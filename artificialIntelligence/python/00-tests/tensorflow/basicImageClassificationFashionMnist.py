#
# TensorFlow and tf.keras
import tensorflow as tf
#
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
#
print(tf.__version__)
#
# Import the Fashion MNIST dataset
# This guide uses the Fashion MNIST dataset which contains 70,000 grayscale images in 10 categories.
# The images show individual articles of clothing at low resolution (28 by 28 pixels).
# Import and load the Fashion MNIST data directly from TensorFlow:
fashion_mnist = tf.keras.datasets.fashion_mnist
#
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
#
# Each image is mapped to a single label.
# Since the class names are not included with the dataset,
# store them here to use later when plotting the images:
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
#
# Explore the data
# Let's explore the format of the dataset before training the model.
# The following shows there are 60,000 images in the training set, with each image represented as 28 x 28 pixels:
print(train_images.shape)
# Likewise, there are 60,000 labels in the training set:
print(len(train_labels))
# Each label is an integer between 0 and 9:
print(train_labels)
# There are 10,000 images in the test set. Again, each image is represented as 28 x 28 pixels:
print(test_images.shape)
# And the test set contains 10,000 images labels:
print(len(test_labels))
#
# Preprocess the data
# The data must be preprocessed before training the network.
# If you inspect the first image in the training set, you will see that the pixel values fall in the range of 0 to 255:
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
#
# Scale these values to a range of 0 to 1 before feeding them to the neural network model.
# To do so, divide the values by 255.
# It's important that the training set and the testing set be preprocessed in the same way:
train_images = train_images / 255.0
test_images = test_images / 255.0
#
# To verify that the data is in the correct format and that you're ready to build and train the network,
# let's display the first 25 images from the training set and display the class name below each image.
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
