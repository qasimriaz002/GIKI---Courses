import nltk

# Importing the re for using the regular expression to remove the words ending with 'ing' string.

import re
from nltk.corpus import gutenberg


nltk.download('punkt')  # downloading the tokenizer
nltk.download('gutenberg')  # downloading the Gutenberg data-set from nltk corpora

# Getting raw string


raw_text = gutenberg.raw('shakespeare-hamlet.txt')
print(raw_text)

# tokenizing using the nltk


words = nltk.word_tokenize(raw_text)

# Displaying the tokens

print(words)

# Regexp for the words ending in the 'ing'


ing_words = [word for word in words if re.search('ing$', word)]

# Displaying the ing words


print(ing_words)

# Finding the words which have any vowel letter before the 'ing' in any word


vovel_ing_words = [word for word in words if re.search('[aeiou].*ing$', word)]

# Showing the list of words which have any vowel letter before the 'ing'


print(vovel_ing_words)

# In[ ]:
