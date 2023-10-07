import nltk

# Stemming Demo

from nltk.stem import PorterStemmer #import class
porter = PorterStemmer() # create instance

porter.stem('walking')
porter.stem('walked')
porter.stem('walks    ') # returns walks, careful about whitespace
porter.stem('walks') # returns walk

porter.stem('ran') # does not change into run
porter.stem('running')

porter.stem('was')
porter.stem('is')
porter.stem('better') # does not work with irregulars

porter.stem('bosses') # changes to boss

porter.stem('replacement') # removes -ement, results in replac

porter.stem('unnecessary') # returns unnecessari, y turns into i, un- should not be removed
porter.stem('berry')

sentence = "Lemmatization is more sophisticated than stemming".split()
for token in sentence:  # use token instead of word
    print(porter.stem(token))