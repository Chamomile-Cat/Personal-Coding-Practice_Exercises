
from sklearn.feature_extraction.text import CountVectorizer

# The Countvectorizer class changes documents into vectors by counting

corpus = [
 'This is the first phrase',
 'This is the first sentence',
 'This the second sentence'
]

vectorizer = CountVectorizer(stop_words='english')  # Initializie CountVector Object
Xtrain = vectorizer.fit_transform(corpus) # Create count vectors on training data

# print(Xtrain) # (sentence index in corpus, specific unique word), how many times the word appears 
# print(vectorizer.get_feature_names_out())

Xtest = vectorizer.transform(corpus) # Transform the training corpus
print(Xtest)




