#
# 
# ------------------------------------------------------------------------------------------ #
# -------------- Setup
# ------------------------------------------------------------------------------------------ #
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
#
# Test Tensorlflow
print("\nTensorflow Version : ", tf.__version__)
#
# Download the dataset : Flower dataset
import pathlib
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(origin=dataset_url, 
                                   fname='flower_photos', 
                                   untar=True)
data_dir = pathlib.Path(data_dir)
#
image_count = len(list(data_dir.glob('*/*.jpg')))
print("Total images in dataset : ", image_count)
#
# An example from dataset :
roses = list(data_dir.glob('roses/*'))
img = PIL.Image.open(str(roses[0]))
img.show()
#
# Another example from dataset :
roses = list(data_dir.glob('roses/*'))
img2 = PIL.Image.open(str(roses[1]))
img2.show()
#
# ------------------------------------------------------------------------------------------ #
# -------------- keras.preprocessing()
# ------------------------------------------------------------------------------------------ #
#
# ------ Create dataset ---------------------------------------------------
#Define some parameters
batch_size = 32
img_height = 180
img_width = 180
#
# extracting tarining data from dataset
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2, #80% of the images for training, and 20% for validation
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
#
# extracting training data from dataset
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2, #80% of the images for training, and 20% for validation
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
#
# examine classes for training and validation
train_class_names = train_ds.class_names
print("\n")
print("Training dataset classes : ", train_class_names)
#
val_class_names = train_ds.class_names
print("Validation dataset classes : ", val_class_names)
#
# ------------------------------------------------------------------------------------------ #
# -------------- Visualize the data
# ------------------------------------------------------------------------------------------ #
#
# Here are the first 9 images from the training dataset
# You can train a model using these datasets by passing them to model.fit 
import matplotlib.pyplot as plt
#
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")
#
# If you like, you can also manually iterate over the dataset and retrieve batches of images
for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break
#
# The image_batch is a tensor of the shape (32, 180, 180, 3). 
# This is a batch of 32 images of shape 180x180x3 (the last dimension referes to color channels RGB). 
# The label_batch is a tensor of the shape (32,), these are the corresponding labels to the 32 images.
# Note : We can call .numpy() on either of these tensors to convert them to a numpy.ndarray.
#
# ------------------------------------------------------------------------------------------ #
# -------------- Standardize the data
#
#The RGB channel values are in the [0, 255] range. 
# This is not ideal for a neural network; 
# in general you should seek to make your input values small. 
# Here, we will standardize values to be in the [0, 1] by using a Rescaling layer.
# ------------------------------------------------------------------------------------------ #
#
from tensorflow.keras import layers
#
normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
#
# There are two ways to use this layer.
# You can apply it to the dataset by calling map:
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixels values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))
#
# Or, you can include the layer inside your model definition to simplify deployment. 
# Note: If you would like to scale pixel values to [-1,1] 
#       you can instead write Rescaling(1./127.5, offset=-1)
#
# ------------------------------------------------------------------------------------------ #
# -------------- Configure the dataset for performance
#
# Let's make sure to use buffered prefetching so we can yield data from disk without having I/O become blocking. 
# These are two important methods you should use when loading data.
#
# .cache() keeps the images in memory after they're loaded off disk during the first epoch. 
#   This will ensure the dataset does not become a bottleneck while training your model. 
#   If your dataset is too large to fit into memory, you can also use this method to create a performant on-disk cache.
#
# .prefetch() overlaps data preprocessing and model execution while training.

#   Interested readers can learn more about both methods, as well as how to cache data to disk in the data performance guide
#   check : https://www.tensorflow.org/guide/data_performance#prefetching
# ------------------------------------------------------------------------------------------ #
#
AUTOTUNE = tf.data.AUTOTUNE
#
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
#
# ------------------------------------------------------------------------------------------ #
# -------------- Train the Model
# ------------------------------------------------------------------------------------------ #
num_classes = 5
#
model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255),
  layers.Conv2D(32, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])
#
model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])
#
# train for a few epochs so this tutorial runs quickly.
model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=3
)