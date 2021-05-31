#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Import required modules
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Load input data text
gloveInput = r'D:\\Libraries\Datasets\\NLP\\GloVe\\glove.6B.100d.txt'
word2vecOutput = 'glove.word2vec'
glove2word2vec(gloveInput, word2vecOutput)
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Create GloVe model
model = KeyedVectors.load_word2vec_format(word2vecOutput, binary=False)
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Examine the vetors and model
#
# to see vector of any word in datatext
print("*\n*")
print("Vector of 'Istanbul' word : \n", model['ring'])
#
# to seemost similar words of any word in datatext
print("*\n*")
print("Similar words with 'Istanbul' word : \n", model.most_similar('gandalf'))
#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# Vector aritmetics ????? >>>>>> THAT IS SO COOL
print("*\n*")
print("* * * * * * VECTOR ARITMETIC OPERATIONS FOR WORD VECTORS * * * * * *")
print("*\n*")
#
# Vector substraction example : king - man + woman = queen
# topn = 1 : show only 1 result( best result)
vec = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print("*\n*")
print("king - man + woman = queen : ", vec )
#
# Vector substraction example : father - man + woman = mother?
# topn = 2 : show 2 result (top 2 result)
vec = model.most_similar(positive=['father', 'woman'], negative=['man'], topn=1)
print("*\n*")
print("father - man + woman = ?? : ", vec )
#
# Vector substraction example : son - man + woman = daughter?
# topn = 2 : show 2 result (top 2 result)
vec = model.most_similar(positive=['woman', 'son'], negative=[ 'man'], topn=1)
print("*\n*")
print("son - man + woman = = ?? : ", vec )
#
# Another random example
# topn = 1 : show only 1 result( best result)
vec = model.most_similar(positive=['ankara', 'germany'], negative=['berlin'], topn=1)
print("*\n*")
print("germany - berlin + ankara = = ?? : ", vec )
#

model.most_similar(positive=['teach', 'doctor'], negative=['treat'], topn=1)
#
