#
#
#   Autoencoders : 
#       - A kind of unsupervised learning methods
#       - Keras reference > https://blog.keras.io/building-autoencoders-in-keras.html 
# 
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Import required modules
from keras.models import Model
from keras.layers import Input, Dense
from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import json, codecs
import warnings
#
warnings.filterwarnings("ignore")
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Load and examine the dataset : 
#       Remember : that metod is a kind of unsupervised leaarning
#                  so, we do not have any label in our dataset.
(xTrain, _), (xTest, _) = fashion_mnist.load_data()
#
xTrain = xTrain.astype("float32") / 255.0
xTest = xTest.astype("float32") / 255.0
#
xTrain = xTrain.reshape((len(xTrain), xTrain.shape[1:][0]*xTrain.shape[1:][1]))
xTest = xTest.reshape((len(xTest), xTest.shape[1:][0]*xTest.shape[1:][1]))
#
plt.imshow(xTrain[4000].reshape(28,28))
plt.axis("off")
plt.show()
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Build keras autoencoder model
#
# | Input Layer | > |Encoder Layer| > |Encoder Layer|>|Decoder Layer|>|Decoder Layer (Output)|
# | 784 Neurons | > |32 Neurons   | > |16 Neurons   |>|32 Neurons   |>| 784 Neurons          |
#   
# Create input layer 
inputImg = Input(shape = (784,))
#Create encoder layer and cnnect it to input layer
encoderLayer = Dense(32, activation="relu")(input_img)
#Create another encoder layer and conncet it to previous encoder layer
encoderLayer = Dense(16, activation="relu")(encoderLayer)
#Create decoder layer and connect it to the previous encoder layer
decoderLayer = Dense(32, activation="relu")(encoderLayer)
#Create another decoder layer and connect it to the previous decoder layer
outputLayer = Dense(784, activation="sigmoid")(decoderLAyer)
#
# Store all layers in keras model : 
autoencoder = Model(inputImg,outputLayer)
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Compile the model
autoencoder.compile(optimizer="rmsprop",loss="binary_crossentropy")
#
# Output and Input must be same : xTrain
#   Because of the unsupervised learning procedure I guess
hist = autoencoder.fit(xTrain,
                       xTrain,
                       epochs=200,
                       batch_size=256,
                       shuffle=True,
                       validation_data = (xTrain,xTrain))
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Evaluation Section
print(hist.history.keys())
#
plt.plot(hist.history["loss"],label = "Train loss")
plt.plot(hist.history["valLoss"],label = "Validation loss")
#
plt.legend()
plt.show()
#
# Seperate encoder part from autoencoder model to test our model.
#      Think about why. so simple.
encoder = Model(inputImg,encoderLayer)
encodedImg = encoder.predict(xTest)
#
plt.imshow(xTest[1500].reshape(28,28))
plt.axis("off")
plt.show()
#
plt.figure()
plt.imshow(encodedImg[1500].reshape(4,4))
plt.axis("off")
plt.show()
#
# Calculate all test outputs for autoencoder
# We are going to compare them with encoder output
decodedImgs = autoencoder.predict(xTest)
#
# Plot results
n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    # display original image
    ax = plt.subplot(2, n, i+1)
    plt.imshow(xTest[i].reshape(28, 28))
    plt.axis("off")
    #
    # display reconstructed image
    ax = plt.subplot(2, n, i + n+1)
    plt.imshow(decodedImgs[i].reshape(28, 28))
    plt.axis("off")
plt.show()
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Save and Load Model 
#
# save model
# autoencoder.save_weights("autoencoder_model.h5")
#
# save hist
# with open("autoencoders_hist.json","w") as f:
#     json.dump(hist.history,f)
#
# load history
# with codecs.open("autoencoders_hist.json","r", encoding="utf-8")  as f:
#     n = json.loads(f.read())
#
# print loaded history
# print(n.keys())
# plt.plot(n["loss"],label = "Train loss")
# plt.plot(n["valLoss"],label = "Validation loss")
#
