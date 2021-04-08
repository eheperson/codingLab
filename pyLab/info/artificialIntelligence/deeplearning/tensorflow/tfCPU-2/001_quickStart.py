import tensorflow as tf


from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

class tfModel(Model):
  def __init__(self):
    super(tfModel, self).__init__()
    self.conv1 = Conv2D(32, 3, activation='relu')
    self.flatten = Flatten()
    self.d1 = Dense(128, activation='relu')
    self.d2 = Dense(10)

  def call(self, x):
    x = self.conv1(x)
    x = self.flatten(x)
    x = self.d1(x)
    return self.d2(x)

mnist = tf.keras.datasets.mnist

(xTrain, yTrain), (xTest, yTest) = mnist.load_data()

xTrain = xTrain /  255.0
xTest = xTest / 255.0


# Add a channels dimension
xTrain = xTrain[..., tf.newaxis].astype("float32")
xTest = xTest[..., tf.newaxis].astype("float32")

# trainDs = tf.data.Dataset.from_tensor_slices((xTrain, yTrain))
# trainDs = trainDsshuffle(10000)
# trainDs = trainDs.batch(32)
trainDs = tf.data.Dataset.from_tensor_slices((xTrain, yTrain)).shuffle(10000).batch(32)
testDs = tf.data.Dataset.from_tensor_slices((xTest, yTest)).batch(32)

# Create an instance of the model
model = tfModel() 


#Choose a loss function for training (loss object or loss funstion)
lossFunction = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

#Choose an optimizer  for training:
optimizer = tf.keras.optimizers.Adam()

# Select metrics to measure the loss and the accuracy of the model :
#
# Metrics for train section
trainLoss = tf.keras.metrics.Mean(name='trainLoss')
trainAccuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='trainAccuracy')
#
#Metrics for test section
testLoss = tf.keras.metrics.Mean(name='testLoss')
testAccuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='testAccuracy')

# Train The Model
@tf.function
def trainStep(images, labels):
  with tf.GradientTape() as tape:
    # training=True is only needed if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    predictions = model(images, training=True)
    loss = lossFunction(labels, predictions)
  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))

  trainLoss(loss)
  trainAccuracy(labels, predictions)
  
# Test The Model
@tf.function
def testStep(images, labels):
  # training=False is only needed if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  predictions = model(images, training=False)
  t_loss = lossFunction(labels, predictions)

  testLoss(t_loss)
  testAccuracy(labels, predictions)
  
EPOCHS = 5
for epoch in range(EPOCHS):
  # Reset the metrics at the start of the next epoch
  trainLoss.reset_states()
  trainAccuracy.reset_states()
  testLoss.reset_states()
  testAccuracy.reset_states()

  for images, labels in trainDs:
    trainStep(images, labels)

  for test_images, test_labels in testDs:
    testStep(test_images, test_labels)

  template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
  print(template.format(epoch + 1,
                        trainLoss.result(),
                        trainAccuracy.result() * 100,
                        testLoss.result(),
                        testAccuracy.result() * 100))
