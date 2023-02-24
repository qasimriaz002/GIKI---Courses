from sklearn.feature_extraction.text import CountVectorizer

# Here in this file I tried to show the array based representation of BOW on a sample text

paragraph = "John goes to school daily. He studies in fifth class. He is a hardworking student. He loves the school life. Martin also studies in same school. But Martin is not hardworking as John."

# Create an instance of CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the paragraph using CountVectorizer
bow_representation = vectorizer.fit_transform([paragraph])

# Print the bag of words representation
print(vectorizer.get_feature_names_out())
# assigns number to each word and shows its frequency
print(bow_representation.toarray())
