#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Import required modules
import numpy as np
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Load data txt file
f = open('C:\\Users\\kuzub\\Desktop\\nlp\\gensim-word2vec\\hurriyet.txt', 'r', encoding='utf8')
text = f.read()
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Prepare loaded data text
#
# tokenization
# for our dataset, every letter is lower case
# no punctuation marks
# sentences seperated by newline operator
# so we do not need any external module for tokenization
tList = text.split('\n')
print(tList) # comment that line if printin takes long time
#
# Lets print our Tlist
print("*\n*")
print("##### Dataset, first 10, semi-tokenized : ")
print(tList[:10])
#
# Create array to collect tokens
corpus = []
# now it is time
# to tokenize sentences in our data text
for cumle in tList:
    corpus.append(cumle.split())
#
# Lets print some tokenized sentences from our data text
print("*\n*")
print("##### Dataset, first 10, fully-tokenized : ")
print(corpus[:10])
##
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Declare Word2Vec model
model = Word2Vec(corpus, vector_size=100, window=5, min_count=5, sg=1)
#  vector_size : size ofthe word vectors
#  windows     : window size
#  min_count   : ignoring words occuring less than 5 times in the corpus
#  sg          :  declaring we will use skip-gram algorithm
#                   default algorithm is cbow
#                   if we want to use sg we have to use  sg=1 parameter
#                   otherwise cbow will be used
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Examine the model
#
# to see word vector of any word in our dictionary(data text)
model.wv['ankara']
#
# to see most similar words with any word
model.wv.most_similar('youtube')
#
# to save trained model
#model.save('word2vec.model')
#
# to load saved model
#model = Word2Vec.load('word2vec.model')
#
def closestWordsTsnePlot(model, word):
    """
    That function is plotter function
    only purpose of that function is plotting
    """
    # creating empy array to collect closest wods
    word_vectors = np.empty((0,100))
    # create wmpty array to collect input words
    word_labels = [word]
    #
    # find closest words of input words
    close_words = model.wv.most_similar(word)
    # store closest words (axis=0 is important, search it if you forget)
    word_vectors = np.append(word_vectors, np.array([model.wv[word]]), axis=0)
    #
    for w, _ in close_words:
        word_labels.append(w)
        word_vectors = np.append(word_vectors, np.array([model.wv[w]]), axis=0)
    #
    # Plotting via TSNE
    # random_state=0 is important, search it if you forget 
    tsne = TSNE(random_state=0)
    Y = tsne.fit_transform(word_vectors)
    #
    x_coords = Y[:, 0]
    y_coords = Y[:, 1]
    #
    # scatter plot
    plt.scatter(x_coords, y_coords)
    #
    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(5, -2), textcoords='offset points')
    #
    # # showing plot    
    plt.show()
#
closestWordsTsnePlot(model, 'at')