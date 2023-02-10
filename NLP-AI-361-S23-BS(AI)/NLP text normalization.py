# Example of text normalization for input in any model like logistic regression/Naive Bayes and etc. on
# Here I used Natural Language Processing (NLP) data set using the nltk library

import nltk
import random
from nltk.corpus import movie_reviews

# Load the movie reviews dataset from the nltk library
# Load punkt tokenizer
# Load stopwords that will be used to match the same words in the data-set for removal
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# Have a look at the downloaded data_set
loaded_text = nltk.corpus.movie_reviews.raw()
print(loaded_text)

# Have a look at downloaded stopwords
allStopWords = nltk.corpus.stopwords.raw()
print(allStopWords)

# Now Extracting features from the movie reviews data
# Before doing that finding out the structure in data-set in list format
review_list = list(movie_reviews.words())
print(review_list)

# Finding the categories of movies from the movie reviews data - So that we can see will it be a binery or multiclass classification problem
movie_categories = movie_reviews.categories()
print(movie_categories)

# So as we can see we only have two types of categories here --- So it a binery classificaiton problem
# Remember all of our data is present in form of files. Some files contains postive reviews and some contains negative
# Now we are going to create a list of positive and negative reviews so that we can check lenght of each list to find number of files with positive and negative reviews
pos_reviews = movie_reviews.fileids('pos')
neg_reviews = movie_reviews.fileids('neg')
print("Number of files with positive reviews: ", len(pos_reviews))
print("Number of files with negative reviews: ", len(neg_reviews))

# Creating a list containing all the postive & negative reviews
# We can see the names of files printed at index 1 and 1002 of list 'all_reviewfiles' created below
# As per the given index, it means first 1000 files are of negative reviews and next 1000 files are of positive reviews
all_reviewfiles = movie_reviews.fileids()
print(all_reviewfiles[1])
print(all_reviewfiles[1002])

# Now we are checking that how we can find the words of each single movie_review using a single 'fileid' as input argument
# to movie_reviews.words(name of file) function. First printing by name of file, Then printing by passing index of array
# of the list 'all_reviewfiles'.
print(movie_reviews.words('pos/cv002_15918.txt'))
print(movie_reviews.words(all_reviewfiles[1002]))

# So we have total 2000 files 1000 with positive and 1000 with negative reviews
# Now Extracting the features from the movie reviews data-set for further processing and model applicaiton
# for this purpose we are creating a documents list
# Extract features from the movie reviews data
documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))
print(len(documents))
print(documents[1][0])  # It shows the all text of a file we assigned using the movie_reviews.words(fileid)
print("\n--------------------------------------\n")
print(documents[1][1])  # It shows the label of text we assigned using the category

# Now we are shuffleing the documents.
# The documents were shuffled to ensure that the order of the training and testing data is random, and that the classifier is not biased towards one category or the other. This is important because the order in which the data is presented to the classifier can affect its performance, especially if the data is imbalanced or if the samples are not independent and identically distributed.
# By shuffling the documents, we can ensure that the training and testing data is a random sample from the complete set of movie reviews, and that the classifier is not overfitting to a particular subset of the data. This is a common step in the machine learning pipeline, and helps to reduce the risk of overfitting and improve the generalization performance of the model.
random.shuffle(documents)
# View after shuffeling
print(len(documents))
print(documents[1][0])  # It shows the all text of a file we assigned using the movie_reviews.words(fileid)
print("\n--------------------------------------\n")
print(documents[1][1])  # It shows the label of text we assigned using the category

# Now we are going to extract all the words from the movie reviews data-set
# Then we will use nltk.FreqDist function to find the number of times each word repeated in the text.
# Here 'all_words' is the object of nltl.FreqDist() class we will pass all words of text to it.
# The frequency distribution all_words is implemented as a dictionary in Python, where the keys are the words and the values are their frequencies. By using the square brackets [] operator to access the frequency of a word w, the code is effectively counting how many times each word occurs in the movie reviews. The all_words[w.lower()] = all_words[w.lower()] + 1 operation increments the count of the word by 1 each time the word is encountered in the movie reviews.

all_words = nltk.FreqDist()
for w in movie_reviews.words():
    all_words[w.lower()] = all_words[w.lower()] + 1

print(all_words.items())  # showing all words of text of along with number of occurences in a dictionary format.
word_features = list(all_words.keys())[:2000]  # Selecting the first 2000 words a features to reduce feature space
print('\n--------------------------------------\n')
print(word_features)


# Define a function to extract the features of each review (each document will be passed to function as argument then function will find word in each review of that document)
# Then function return a dictonary named as 'features' with the word as the key and a Boolean value indicating whether the word is in the input document.
# The returned dictionary will be used as a feature vector in the training and evaluation of the logistic regression classifier.
# The set(document) command in the document_features function is used to create a set of unique words in the document. A set is a data structure in Python that stores unique elements, and the set creation using set(document) ensures that each word in the document is only counted once.

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:  # Using the top 2000 words we got from the frequencey distribution in previous step
        features[word] = (word in document_words)  # this '(word in document_words)' will return answer in true or false
    return features


# As we do remember that we created the documents list above containing the words/tokens of all files.
# along with their lable/category at the zero and one index of each item. As shown in following two lines:
# print(documents[0][0])
# print(documents[0][1])

# Now we want to extract the features from the movie reviews data
# We will create a list name featuresets containing the data of all features of all reviews of all data files.
# This list 'featuresets' will contain 2000 thousand tuples in it each containing two items a file/document and it's label.
# Then each of that tuple will 2000 dictionaries because we choose top 2000 words to check in each reviews of each document that it exits or not.
# These dictionaries will contain the works along with the 'true/false' values against each word

featuresets = []
for (d, c) in documents:  # d means document, c means category/label
    featuresets.append((document_features(d), c))

print('Lenght of Feature Set: ', len(featuresets))
print('Type of Feature Set: ', type(featuresets))
print('\n--------------------------------------\n')

print('Lenght of element inside the Feature Set: ', len(featuresets[0]))
print('Type of element inside the Feature Set: ', type(featuresets[0]))
print('\n--------------------------------------\n')

print('Lenght of element inside the Tuple: ', len(featuresets[0][0]))
print('Type of element inside the Tuple: ', type(featuresets[0][0]))
print('\n--------------------------------------\n')

print('Lenght of dictionary inside the Tuple: ', len(list(featuresets[0][0].items())[0]))
print('Sample item of a dictionary: ', list(featuresets[0][0].items())[0])
print('\n--------------------------------------\n')

print('Sample Feature Set at 0 index is shown below')
print(featuresets[0][0])
print('\n--------------------------------------\n')
print('Lable/Category of sample Feature Set at 0 index is shown below:')
print(featuresets[0][1])

# ------------------------------ NOW WE CAN GIVE THESE FEATURES TO ANY ML BASED MODEL LIKE LOG-REG, NAIVE-B AND ETC.
