# in this example I used Ngrams functions from nltk library
# the function is used to perform the N-Grams based POS-Tag analysis at Movie Reviews Data-Set.

import nltk
from nltk.corpus import movie_reviews
from nltk import ngrams

nltk.download('movie_reviews')
nltk.download('averaged_perceptron_tagger')

# define the target pattern and the size of the n-grams
pattern = "JJ NN"
n = 2

# create the POS tag N-grams of the movie reviews
pos_ngrams = []
for fileid in movie_reviews.fileids():
    words = movie_reviews.words(fileid)
    tags = [tag for word, tag in nltk.pos_tag(words)]
    pos_ngrams += ngrams(tags, n)
print(len(pos_ngrams))
print(pos_ngrams[0:50])

# find the samples that match the target pattern
matched_samples = []
for fileid in movie_reviews.fileids():
    words = movie_reviews.words(fileid)
    tags = [tag for word, tag in nltk.pos_tag(words)]
    tag_ngrams = ngrams(tags, n)
    for i, gram in enumerate(tag_ngrams):
        if " ".join(gram) == pattern:
            matched_samples.append(" ".join(words[i:i+n]))

# print the frequency and the first 50 matched samples of the target pattern
print("Frequency of pattern '{}': {}".format(pattern, pos_ngrams.count(pattern.split())))
print("First 50 matched samples:")
for sample in matched_samples[:50]:
    print(sample)

# find the samples that match the target pattern
matched_samples = []
matched_pos_tags = []
for fileid in movie_reviews.fileids():
    words = movie_reviews.words(fileid)
    tags = [tag for word, tag in nltk.pos_tag(words)]
    tag_ngrams = ngrams(tags, n)
    for i, gram in enumerate(tag_ngrams):
        if " ".join(gram) == pattern:
            matched_samples.append(" ".join(words[i:i+n]))
            matched_pos_tags.append(" ".join(tags[i:i+n]))
print(len(matched_samples))
print(len(matched_pos_tags))

# print the frequency and the first 50 matched samples of the target pattern
print("Frequency of pattern '{}': {}".format(pattern, pos_ngrams.count(pattern.split())))
print("First 50 matched samples:")
for i in range(50):
    print("{}: {}".format(matched_samples[i], matched_pos_tags[i]))

