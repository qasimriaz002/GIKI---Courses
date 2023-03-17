# I created this file to create he uni-grams, big-rams and tri-grams without using the strings manipulation and loops
# No any library like NLTK is not used.
# At last countVectorizer is used to generate ngrams features
text = "The quick brown fox jumps over the lazy dog"
words = text.split()
words

# create bigrams
bigrams = []
for i in range(len(words) - 1):
    bigrams.append(words[i] + " " + words[i + 1])
bigrams

# create trigrams
trigrams = []
for i in range(len(words) - 2):
    trigrams.append(words[i] + " " + words[i + 1] + " " + words[i + 2])
trigrams

# create bag of words representations
bow_bigrams = {}
for bigram in bigrams:
    if bigram in bow_bigrams:
        bow_bigrams[bigram] += 1
    else:
        bow_bigrams[bigram] = 1
bow_bigrams

bow_trigrams = {}
for trigram in trigrams:
    if trigram in bow_trigrams:
        bow_trigrams[trigram] += 1
    else:
        bow_trigrams[trigram] = 1
bow_trigrams

print(len(words))
print(len(bigrams))
print(len(trigrams))

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# example data
texts = ["The quick brown fox jumps over the lazy dog",
         "She sells seashells by the seashore",
         "How much wood would a woodchuck chuck",
         "Red lorry, yellow lorry, red lorry, yellow lorry"]

labels = ["animals", "beach", "wood", "vehicles"]

# create bigrams from the texts
vectorizer = CountVectorizer(ngram_range=(2, 2))
X = vectorizer.fit_transform(texts)

X

X.toarray()[1]

vectorizer.get_feature_names_out()
