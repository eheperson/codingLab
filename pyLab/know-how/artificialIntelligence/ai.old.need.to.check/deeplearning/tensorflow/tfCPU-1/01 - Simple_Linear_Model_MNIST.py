import tensorflow as tf

from tensorflow.examples.tutorials.mnist import  input_data

#Reading Input Data
mnist = input_data.read_data_sets("../data/MNIST", one_hot=True)

# Placeholder for input(x) and target(y_true)
x = tf.placeholder(tf.float32, [None,784]) # (dataType, [howManyImageWillCome, ImageDimensions])

y_true = tf.placeholder(tf.float32, [None,10])

#Variables
# x = [500,784]
# w = [784,10]
# b = [10 , 1]
# x*w = [500,10]

w = tf.Variable(tf.zeros([784,10]))

b = tf.Variable(tf.zeros([10]))

# y = x*w + b  y:logits
# softmax -> 0:1

logits = tf.matmul(x, w) + b
y = tf.nn.softmax(logits)

#loss function = crossentrophy
#cross_entrophy has its own soft_ma before calculation
xent = tf. nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_true)
# calculating mean of xent (loss)
loss = tf.reduce_mean(xent)

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_true,1))
#arr = [0,0,1,0]
#in = tf.argmax(arr,1)
# value of in will be 2 (the index of 1)

#correct_prediction is boolean
#we have to cast it to float32 
correct_prediction = tf.cast(correct_prediction, tf.float32)

accuracy = tf.reduce_mean(correct_prediction)

optimize = tf.train.GradientDescentOptimizer(0.5)

optimize = optimize.minimize(loss) #we try to minimize loss value

sess = tf.Session()
sess.run(tf.global_variables_initializer())



def training_step(iterations, batch_size):
    for i in range(iterations):
        x_batch, y_batch = mnist.train.next_batch(batch_size)
        feed_dict_train = {x: x_batch, y_true:y_batch}
        sess.run(optimize, feed_dict=feed_dict_train)
        
def test_accuracy():
    feed_dict_test = {x:mnist.test.images, y_true:mnist.test.labels}
    acc = sess.run(accuracy, feed_dict=feed_dict_test)
    print("Test Accuracy : ", acc)

batchSize = 128    
training_step(2000, batchSize)
test_accuracy()
        
    