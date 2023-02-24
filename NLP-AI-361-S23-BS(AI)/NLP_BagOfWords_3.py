# Bag of words without using Count-Vectorizer
# Just a simple of Example of BOW from scratch using the counter and tokenizer only

import re
from collections import Counter

paragraph = "John goes to school daily. He studies in fifth class. He is a hardworking student. He loves the school life. Martin also studies in same school. But Martin is not hardworking as John."

# Preprocess the paragraph by converting all characters to lowercase and removing non-alphabetic characters
processed_paragraph = re.sub(r'\W+', ' ', paragraph.lower())

# Tokenize the paragraph by splitting it into individual words
tokens = processed_paragraph.split()

# Create a dictionary to store the bag of words representation of the paragraph
bow = Counter(tokens)

# Print the bag of words representation
print(bow)