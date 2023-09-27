
corpus = input('Enter in your data with commas separating each sentence: ')

corpus = corpus.lower()
corpus = corpus.split(", ")

unique_words = set() # Set of unique words
total_tokens = [] # List of all tokens
for sentence in corpus: # Create
    words = sentence.split()
    unique_words.update(words)
    for i in words:
        total_tokens.append(i) 

count_vectors = dict.fromkeys(unique_words, 0) # Count frequencies of each unique token
for word1 in count_vectors.keys():
    for word2 in total_tokens:
        if word1 == word2:
            count_vectors[word1] = count_vectors[word1] + 1
