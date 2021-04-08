import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
#
#
#######3  Sentiment analysis
#
# This notebook trains a sentiment analysis model to classify movie reviews 
# as positive or negative, based on the text of the review. 
# This is an example of binary—or two-class—classification, an important 
# and widely applicable kind of machine learning problem.

# You'll use the Large Movie Review Dataset that contains the text 
# of 50,000 movie reviews from the Internet Movie Database. 
# These are split into 25,000 reviews for training and 25,000 reviews 
# for testing. The training and testing sets are balanced, meaning 
# they contain an equal number of positive and negative reviews.



url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file("aclImdb_v1.tar.gz", url,
                                    untar=True, cache_dir='.',
                                    cache_subdir='')

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

os.listdir(dataset_dir)

train_dir = os.path.join(dataset_dir, 'train')
os.listdir(train_dir)

sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
with open(sample_file) as f:
    print(f.read())