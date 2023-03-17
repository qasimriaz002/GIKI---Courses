# Hello Students
# In this example I used the minimum edit distance to find the nearest right spellings for the wrong english word.

import numpy as np


def min_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        dp[i, 0] = i

    for j in range(n + 1):
        dp[0, j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i, j] = dp[i - 1, j - 1]
            else:
                dp[i, j] = 1 + min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1])

    return dp[m, n]


# List of some correct words
words = ['hello', 'world', 'python', 'programming', 'code', 'example']

# Sample Misspelled word
misspelled_word = 'exampel'

# Calculate the minimum edit distance between the misspelled word and each word in the list, and print the
# weight/cost of difference for each word
for word in words:
    distance = min_edit_distance(misspelled_word, word)
    print(f"The weight/cost of difference between '{misspelled_word}' and '{word}' is {distance}")

# Find the index of the word with the minimum distance
distances = [min_edit_distance(misspelled_word, word) for word in words]
min_index = distances.index(min(distances))

# Print the nearest correct spelling
print(f"The nearest correct spelling for '{misspelled_word}' is '{words[min_index]}'")
