# # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #
# # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #
# # #
# # Dil Çeşitleri :
# # #
# #     > Makine Dilleri :
# #         - C++, Java, Python...
# #         - Az sayıda kelime bulunur.
# #         - BElirli kuralları vardır ve bu kuralların dışına çıkılamaz.
# # #   
# #     > Doğal Diller : 
# #         - Türkçe, İngilizce, Japonca.
# #         - Çok fazla kelime bulunur.
# #         - Kesin kuralları yotur.
# #         - SOnsuz sayıda kelime kombinasyonu olabilir.
# # #
# # #
# # #
# # #
# # Doğal dil işleme düşük seviyeden yüksek seviyeye geniş bir yelpazede 
# # birçok görev için kullanılır. Bazı temel örnekeler şu şekildedir :
# # #
# #     > Yazım denetimi, autocorrect, eşanlam bulma, anahtar kelime arama.
# #     > Yazlardan, websitelerinin bilgi çıkarması : Ürün fiyatları, tarihler, yerler, kişi ve şirket isimleri..
# #     > Sınıflandırma : OLumlu/Olumsuz, Spam/SpamDeğil, makalenın konusu, kitabın yazarı.
# #     > Makine çevirisi.
# #     > Chatbotlar.
# #     > Soru-cevap sistemleri.
# # #
# # #
# # #
# # Doğal dil işleme neden gereklidir?
# # #
# #     > İnsanların ömür boyunca edindiği görsel, durumsal, işitsel tecrübeleri sadece yazı ile bilgisayara aktarmak zordur.
# #     > Makine dillerine göre doğal diller çok daha fazla kelimeye sahiptir.
# #     > Kelimelerin birden fazla anlamları vardır.
# #     > Kelime oyunlarını bilgisayarların anlaması zordur.
# #     > Doğal dillerin genel kuralları olsa da bu kuralların dışına sıklıkla çıkılır.
# #     > Dünyada şu anda konuşulan 6500 civarında farklı dil vardır.
# # #
# # #
# # #
# # Corpus and Corpora :
# # #
# #     > In linguistics, a corpus (plural corpora) or text corpus is a language resource consisting of 
#         a large and structured set of texts (nowadays usually electronically stored and processed). In corpus linguistics, 
#         they are used to do statistical analysis and hypothesis testing, checking occurrences or 
#         validating linguistic rules within a specific language territory.
# # #
# # #
# # #
# # Corpus Resources :
# # #   > Kaggle
# #     > Gutenberg Project
# #     > Wikipedia
# #     > Common Crawl
# # 
# # 
# # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #
# # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# IMPORT REQUIRED MODULES
import nltk
# Modules for tokenizing
from nltk.tokenize import sent_tokenize, word_tokenize
# Module for stop-words
from nltk.corpus import stopwords
# Module forstemming
from nltk.stem import PorterStemmer
# Module for part of speech tagging
from nltk import pos_tag
# Module for named entity recognition
from nltk import ne_chunk
# Module for lemmatizing
from nltk.stem import WordNetLemmatizer
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# DOWNLOAD required DATA from NLTK
# if any data error, uncomment :
#nltk.download()
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# TOKENIZING
print("\n* *\n* *\n* *\n")
text = "Alan Turing, İngiliz matematikçi, bilgisayar bilimcisi ve kriptolog. Bilgisayar biliminin kurucusu sayılır. Geliştirmiş oldugu Turing testi ile makinelerin ve bilgisayarların düşünme yetisine sahip olup olamayacakları konusunda bir kriter öne sürmüştür."
text.split()
#
# Tokenizing words
word_tokenize(text)
#
for token in word_tokenize(text):
    print(token)
#
# Convert all sentence to 1 token
sent_tokenize(text)
#
for token in sent_tokenize(text):
    print(token)
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# STOP WORDS  
# (stop word : unrequired word, 
#  in english : a, an, the ...)
print("\n* *\n* *\n* *\n")
text = 'Fazıl Say is a Turkish pianist and composer who was born in Ankara, described recently as "not merely a pianist of genius; but undoubtedly he will be one of the great artists of the twenty-first century".'
#
# To detect stopwords in our corpus
# we need to store all stop-words of language
stopwords = stopwords.words('english')
#
print(" Stop Words in Turkish : ", stopwords.words('turkish'))
print(" Stop Words in English : ", stopwords.words('english'))
#
# tokenezing  our sentence
words = word_tokenize(text)
#
# Filtering our sentence from stop words
filtered_words = []
for word in words:
    if word not in stopwords:
        filtered_words.append(word)
#
print(filtered_words)
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# STEMMING
# stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form—generally 
# a written word form. The stem need not be identical to the morphological root of the word; 
# it is usually sufficient that related words map to the same stem, even if this stem is not in itself a valid root.
#  stem of the 'running' is 'run')
print("\n* *\n* *\n* *\n")
#
ps = PorterStemmer()
#
# select words to stemming process
words = ['drive', 'driving', 'driver', 'drives', 'drove', 'cats', 'children']
# porterStemmer only looks at the end of the word
# so, it will not so succesfull for children and drove
#
for w in words:
    print(ps.stem(w))
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# PART of SPEECH TAGGING
print("\n* *\n* *\n* *\n")
#
text = 'Friedrich Wilhelm Nietzsche was a German philosopher, cultural critic, composer, poet, philologist, and a Latin and Greek scholar whose work has exerted a profound influence on Western philosophy and modern intellectual history. He began his career as a classical philologist before turning to philosophy. He became the youngest ever to hold the Chair of Classical Philology at the University of Basel in 1869 at the age of 24. Nietzsche resigned in 1879 due to health problems that plagued him most of his life; he completed much of his core writing in the following decade. In 1889 at age 44, he suffered a collapse and afterward, a complete loss of his mental faculties. He lived his remaining years in the care of his mother until her death in 1897 and then with his sister Elisabeth Förster-Nietzsche. Nietzsche died in 1900.'
#
tokenized = word_tokenize(text)
#
print(pos_tag(tokenized))
## If proper names do not start with a capital letter, 
## it may not be successful.
#
#   ALL ABBREVATIONS : 
# CC     coordinating conjunction
# CD     cardinal digit
# DT     determiner
# EX     existential there (like: "there is" ... think of it like "there exists")
# FW     foreign word
# IN     preposition/subordinating conjunction
# JJ     adjective 'big'
# JJR    adjective, comparative 'bigger'
# JJS    adjective, superlative 'biggest'
# LS     list marker 1)
# MD     modal could, will
# NN     noun, singular 'desk'
# NNS    noun plural 'desks'
# NNP    proper noun, singular 'Harrison'
# NNPS   proper noun, plural 'Americans'
# PDT    predeterminer 'all the kids'
# POS    possessive ending parent's
# PRP    personal pronoun I, he, she
# PRP$   possessive pronoun my, his, hers
# RB     adverb very, silently,
# RBR    adverb, comparative better
# RBS    adverb, superlative best
# RP     particle give up
# TO     to go 'to' the store.
# UH     interjection errrrrrrrm
# VB     verb, base form take
# VBD    verb, past tense took
# VBG    verb, gerund/present participle taking
# VBN    verb, past participle taken
# VBP    verb, sing. present, non-3d take
# VBZ    verb, 3rd person sing. present takes
# WDT    wh-determiner which
# WP     wh-pronoun who, what
# WP$    possessive wh-pronoun whose
# WRB    wh-abverb where, when
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# NAMED ENTITY RECOGNITION
# ( It is a process of information extraction that seeks to locate and classify named entities mentioned 
# in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, 
# time expressions, quantities, monetary values, percentages, etc.)
print("\n* *\n* *\n* *\n")
#
text = "Steve Jobs was an American entrepreneur and business magnate. He was the chairman, chief executive officer (CEO), and a co-founder of Apple Inc., chairman and majority shareholder of Pixar, a member of The Walt Disney Company's board of directors following its acquisition of Pixar, and the founder, chairman, and CEO of NeXT. Jobs is widely recognized as a pioneer of the microcomputer revolution of the 1970s and 1980s, along with Apple co-founder Steve Wozniak. "
#
tokenized = word_tokenize(text)
#
tagged = pos_tag(tokenized)
#
namedEnt = ne_chunk(tagged)
#
namedEnt.draw()
# 
# NE Türü         	Örnek
# ORGANIZATION    	Georgia-Pacific Corp., WHO
# PERSON          	Eddy Bonte, President Obama
# LOCATION        	Murray River, Mount Everest
# DATE            	June, 2008-06-29
# TIME            	two fifty a m, 1:30 p.m.
# MONEY           	175 million Canadian Dollars, GBP 10.40
# PERCENT         	twenty pct, 18.75 %
# FACILITY        	Washington Monument, Stonehenge
# GPE             	South East Asia, Midlothian
# 
#
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------ #
# LEMMATIZING
# Lemmatisation (or lemmatization) in linguistics is the process of grouping together the inflected 
# forms of a word so they can be analysed as a single item, identified by the word's lemma, or dictionary form.
#
lem = WordNetLemmatizer()
#
words = ['drive', 'driving', 'driver', 'drives', 'drove', 'cats', 'children']
#
for w in words:
    print(lem.lemmatize(w))
#
lem.lemmatize('drove', 'v')
#
# Lemmatizing is better than stemming !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
