import nltk
from nltk.corpus import movie_reviews
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

# Download the movie_reviews corpus if not already available
nltk.download('movie_reviews')

# Load the corpus and preprocess the data
raw_text = []
for fileid in movie_reviews.fileids():
    raw_text.append(movie_reviews.raw(fileid))

text = []
for document in raw_text:
    tokens = word_tokenize(document)
    stemmer = PorterStemmer()
    text.append(" ".join([stemmer.stem(word.lower()) for word in tokens if word.isalpha()]))

# Create a bag of words model
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(text)

# Get the vocabulary and feature names
vocab = vectorizer.vocabulary_
features = vectorizer.get_feature_names_out()

# Print the results
print("Vocabulary size: ", len(vocab))
print("First 10-60 features: ", features[10:50])
print("---------------------")
print("Last 50 features: ", features[24808:24868])
