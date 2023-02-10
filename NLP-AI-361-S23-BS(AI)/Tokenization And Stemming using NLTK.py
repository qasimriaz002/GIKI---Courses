# importing NLTK and different elements that we need in this file
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download()  # Use this command to download the corpus and functions/models we need to use in our project

from nltk.corpus import gutenberg  # importing the corpus as data-set

hamlet = gutenberg.raw('shakespeare-hamlet.txt')  # converting it into a raw string

tokens = word_tokenize(hamlet)  # performing tokenization
print(tokens)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]  # performing lemmatization
print(stemmed_words)
