# Stemming using NlTK
from nltk.stem import PorterStemmer

porter = PorterStemmer() # initialize object

porter.stem('walking') # is walk
porter.stem('better') # is beter
porter.stem('mossed') # is moss

# Lemmitization using NLTK
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# nltk.download('wordnet') # only once

lemmatizer = WordNetLemmatizer()  # initialize object


lemmatizer.lemmatize('walking') # is walking
lemmatizer.lemmatize('walking', pos=wordnet.NOUN) # is waling
lemmatizer.lemmatize('walking', pos=wordnet.VERB) # is walk
lemmatizer.lemmatize('better', pos=wordnet.ADJ) # is good
lemmatizer.lemmatize('mossed') # is mossed