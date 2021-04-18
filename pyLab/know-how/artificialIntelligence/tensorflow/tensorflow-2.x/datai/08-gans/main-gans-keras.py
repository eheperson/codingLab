#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Import required libraries
from keras.layers import Dense, Dropout, Input, ReLU
from keras.models import Model, Sequential
from keras.optimizers import Adam
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
#
import ganKeras as ganModule
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# Load and examine dataset
(xTrain, tTrain), (xTest, tTest) = mnist.load_data()
xTrain = (xTrain.astype(np.float32)-127.5)/127.5
#
print(xTrain.shape)
#
xTrain = xTrain.reshape(xTrain.shape[0],xTrain.shape[1]*xTrain.shape[2])
print(xTrain.shape)
#
#plt.imshow(xTest[12])
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# build generator
g = ganModule.generatorBuilder()
g.summary()   
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# build discriminator
d = ganModule.discriminatorBuilder()
d.summary()
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
#build GAN network
gan = ganModule.GANbuilder(d, g)
gan.summary()
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# train
#
epochs = 50
batch_size = 256
#
for e in range(epochs):
    for _ in range(batch_size):
        #
        noise = np.random.normal(0,1, [batch_size,100])
        #
        generatedImgs = g.predict(noise)
        #
        imgBatch = xTrain[np.random.randint(low = 0, high = xTrain.shape[0],size = batch_size)]
        #
        x = np.concatenate([imgBatch, generatedImgs])
        #
        yDicsriminator = np.zeros(batch_size*2)
        yDicsriminator[:batch_size] = 1
        #
        d.trainable = True
        d.train_on_batch(x,yDicsriminator)
        #
        noise = np.random.normal(0,1,[batch_size,100])
        #
        yGenerator = np.ones(batch_size)
        #
        d.trainable = False
        #
        gan.train_on_batch(noise, yGenerator)
    print("epochs: ",e)
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# visualize
noise= np.random.normal(loc=0, scale=1, size=[100, 100])
generatedImgs = g.predict(noise)
generatedImgs = generatedImgs.reshape(100,28,28)
plt.imshow(generatedImgs[66], interpolation='nearest')
plt.axis('off')
plt.show()
#
# --------------------------------------------------------------------- # 
# --------------------------------------------------------------------- #
# save
#g.save_weights('GANs-model.h5') 