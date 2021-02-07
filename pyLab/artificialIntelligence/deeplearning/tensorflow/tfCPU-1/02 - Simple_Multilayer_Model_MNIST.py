import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../data/MNIST/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
y_true = tf.placeholder(tf.float32, [None,10])

#dropout
pkeep = tf.placeholder(tf.float32)

layer1 = 120
layer2 = 64
layer3 = 32
layerOut = 10

weight1 = tf.Variable(tf.truncated_normal([784, layer1], stddev=0.1))
bias1 = tf.Variable(tf.constant(0.1, shape=[layer1]))


weight2 = tf.Variable(tf.truncated_normal([layer1, layer2], stddev=0.1))
bias2 = tf.Variable(tf.constant(0.1, shape=[layer2]))


weight3 = tf.Variable(tf.truncated_normal([layer2, layer3], stddev=0.1))
bias3 = tf.Variable(tf.constant(0.1, shape=[layer3]))


weight4 = tf.Variable(tf.truncated_normal([layer3, layerOut], stddev=0.1))
bias4 = tf.Variable(tf.constant(0.1, shape=[layerOut]))

y1 = tf.matmul(x , weight1) + bias1
y1 = tf.nn.relu(y1)
y1d = tf.nn.dropout(y1,pkeep)

y2 = tf.matmul(y1d , weight2) + bias2
y2 = tf.nn.relu(y2)
y2d = tf.nn.dropout(y2,pkeep)


y3 = tf.matmul(y2d , weight3) + bias3
y3 = tf.nn.relu(y3)
y3d = tf.nn.dropout(y3,pkeep)


y4 = tf.matmul(y3d, weight4) + bias4
logits = tf.nn.softmax(y4)

xent = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_true)
loss = tf.reduce_mean(xent)

correct_prediction = tf.equal(tf.argmax(logits,1), tf.argmax(y_true,1))
correct_prediction = tf.cast(correct_prediction, tf.float32)

accuracy = tf.reduce_mean(correct_prediction)

optimize = tf.train.AdamOptimizer(0.001) #learningrate = 0.001
optimize = optimize.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch_size = 128
loss_graph = []

x_batch, y_batch = mnist.train.next_batch(batch_size)
feed_dict_train = {x:x_batch, y_true:y_batch, pkeep:0.75}
feed_dict_test = {x:mnist.test.images, y_true:mnist.test.labels, pkeep:1}

def training_step(iterations):
    for i in range(iterations): 
        [_, train_loss] = sess.run([optimize, loss], feed_dict=feed_dict_train,) 
        
        loss_graph.append(train_loss)
        
        if i % 100 == 0 :
            train_acc = sess.run(accuracy, feed_dict=feed_dict_train)
            print("Iterations : ",i, "  Training Acuracy : ", train_acc, "   Training Loss : ", train_loss)
            
def test_accuracy():
    
    acc = sess.run(accuracy, feed_dict=feed_dict_test)
    print("Test Accuracy : ", acc)
    
    
def plot_images(images, cls_true, cls_pred=None):
    assert len(images) == len(cls_true) == 9
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i].reshape(28, 28), cmap='binary')
        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        ax.set_xlabel(xlabel)
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()


def plot_example_errors():
    mnist.test.cls = np.argmax(mnist.test.labels, axis=1)
    y_pred_cls = tf.argmax(y4, 1)
    correct, cls_pred = sess.run([correct_prediction, y_pred_cls], feed_dict=feed_dict_test)
    incorrect = (correct == False)

    images = mnist.test.images[incorrect]
    cls_pred = cls_pred[incorrect]
    cls_true = mnist.test.cls[incorrect]

    plot_images(images=images[0:9], cls_true=cls_true[0:9], cls_pred=cls_pred[0:9])

  
training_step(10000)
test_accuracy()
plot_example_errors()

plt.plot(loss_graph,'k-')
plt.title('Loss Graph')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.show()

    