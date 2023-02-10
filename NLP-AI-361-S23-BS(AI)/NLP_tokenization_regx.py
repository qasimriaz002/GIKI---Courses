import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
import re

# download and getting a raw string out the of the shakespeare-caesar.txt file


nltk.download('shakespeare')
shakespeare_text = gutenberg.raw('shakespeare-caesar.txt')
print(shakespeare_text)

# Tokenizing the sentence using the nltk library


sentences = sent_tokenize(shakespeare_text)
print(sentences)

# defining a regular expression to do a manual tokenization at words level for each sentence without using nltk.


words = [re.findall(r'\w+', sentence) for sentence in sentences]

# showing the all the words on screen after passing through the RegExp


print(words)

# In following comments i mentioned the working of regexp and symbols used in it

# In this context, \w is a special character class that represents any alphanumeric character (letters or digits)
# or underscore (_). The + symbol following \w specifies that the pattern should match one or more consecutive word
# characters.
