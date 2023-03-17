# Here I am counting the frequency of a specific POS tag pattern
# using N-grams in Python:

from collections import Counter
from nltk import *


download('averaged_perceptron_tagger')

# define the text and the target pattern
text = """Once while traveling, Raman found himself in the company of a group of soldiers.

They were all veterans of war and soon they got to talking about their experiences on the battlefield. One old soldier told of the time he had single-handedly slain seven enemy soldiers. Another gave a detailed description of the manner in which he had held an entire enemy battalion at bay.

When they had finished they looked condescendingly at Raman.

"I don't suppose you have any adventure worth telling," said one of the grizzled warriors.

"Oh, but I have," said Rama

"You have?!" said the soldiers.

"Yes," said Rama. "Once while traveling I chanced upon a large tent. I entered and there, lying on a mat was the largest man I had ever seen. I recognized him at once as a dreaded dacoit who had been terrorizing that part of the country for years!"

"What did you do?" asked the soldiers, their interest now fully aroused.

"I cut off his toe and ran for dear life," said Rama.

"His toe?" said a soldier. "Why toe? You should have cut off his head while you had the chance!"

"Somebody had already done that," said Rama, grinning."""

pattern = "DT NN"

# define the size of the n-grams
n = 2

# create the POS tags of the text
pos_tags = [tag for word, tag in pos_tag(text.split())]
print(pos_tags[:50])

# create the N-grams of the POS tags
pos_ngrams = ngrams(pos_tags, n)

# count the frequency of the target pattern
pos_ngram_counter = Counter([" ".join(gram) for gram in pos_ngrams])
pattern_freq = pos_ngram_counter[pattern]
print(pattern_freq)

# print the frequency of the target pattern
print("Frequency of pattern '{}': {}".format(pattern, pattern_freq))



