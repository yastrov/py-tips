# -*- coding: utf-8 -*-
from __future__ import print_function

__doc__ = """
Test for Naive Bayes from sklearn and nltk library.
Py 2.7
"""

from codecs import open as copen

def read(fname, enc="UTF-8"):
    l = None
    with copen(fname, "r", encoding=enc) as f:
        l = [line.strip() for line in f]
    return l

pos_smiles = read("pos_smiles.txt")
pos_words = read("pos_words.txt")
neg_smiles = read("neg_smiles.txt")
neg_words = read("neg_words.txt")

# cat tweets.json
# [
#     {
#         "created": "2014-02-12",
#         "creator": "A1",
#         "polarity": "positive",
#         "text": "Hello world :)",
#         "confirm": 1,
#         "denied": 0
#     },
#     {
#         "created": "2014-02-12",
#         "creator": "A2",
#         "polarity": "negative",
#         "text": "Hello world :(",
#         "confirm": 1,
#         "denied": 0
#     }
# ]

# NLTK
from nltk import NaiveBayesClassifier

def twit_features(twit):
    assert isinstance(twit, (str, unicode))
    ff = {"pos_smile": pos_smiles,
    "neg_smile": neg_smiles,
    "pos_word": pos_words,
    "neg_word": neg_words}
    features = {}
    twit = twit.lower()
    twitcount = twit.count
    for label, ob in ff.items():
        features[label] = sum([twitcount(mark) for mark in ob])
    return features

class SentimentAnalyzer(object):
    def train(self, training_corpus):
        assert isinstance(training_corpus, (list, tuple))
        assert isinstance(training_corpus[0], dict)
        featureset = [(twit_features(i["text"]), i["polarity"])
                        for i in training_corpus
                        if i["denied"] == 0]
        self.classifier = NaiveBayesClassifier.train(featureset)
        
    def getClasses(self, texts):
        assert isinstance(texts, (list, tuple))
        assert isinstance(texts[0], (str, unicode))
        return [self.classifier.classify(twit_features(i))
                for i in texts]

# sklearn
from sklearn.naive_bayes import GaussianNB

### Analog for your script, return 2D array (best for Gaussian NB)
def twit_feat2(twit):
    assert isinstance(twit, (str, unicode))
    def count(x):
        """
        x is one of each: pos_smiles, neg_smiles, pos_words, neg_words
        """
        twitcount = twit.count
        return sum([twitcount(mark) for mark in x])
    twit = twit.lower()
    return map(count, [pos_smiles, neg_smiles, pos_words, neg_words])


class SentimentAnalyzer2(object):
    def __init__(self):
        self.__d = {0: "negative",
                    1: "neutral",
                    2: "positive"}

    def train(self, training_corpus):
        assert isinstance(training_corpus, (list, tuple))
        assert isinstance(training_corpus[0], dict)
        tp = [] # info for education (result which we want to see)
        tf = [] # array of vectors with info about input
        for i in training_corpus:
            if i["denied"] == 0:
                polarity = i["polarity"]
                tf.append(twit_feat2( i["text"]) ) 
                if "negative" in polarity:
                    tp.append(0)
                elif "neutral" in polarity:
                    tp.append(1)
                elif "positive" in polarity:
                    tp.append(2)
        my_class = GaussianNB()
        my_class.fit(tf, tp)
        self.classifier = my_class
        
    def getClasses(self, texts):
        assert isinstance(texts, (list, tuple))
        assert isinstance(texts[0], (str, unicode))
        # def talk(x):
        #     if x == 0: return "negative"
        #     elif x == 1: return "neutral"
        #     elif x == 2: return "positive"
        predict = self.classifier.predict
        predictF = lambda x: predict(twit_feat2(x))
        d = self.__d
        return map(d.get, map(predictF, texts))


def test():
    import json
    entry = None
    with copen("tweets.json", 'r', encoding="UTF-8") as f:
        entry = json.load(f)
    if entry is None:
        print("Exception: No JSOM file with tweets!")
        exit()

    DataForLearn = entry[80:]
    DataForPredict = [i["text"] for i in entry[:20]]
    # NLTK
    sa = SentimentAnalyzer()
    sa.train(DataForLearn)
    print(sa.getClasses(DataForPredict))

    print "\n"
    # ski-learn
    sa2 = SentimentAnalyzer2()
    sa.train(DataForLearn)
    print(sa.getClasses(DataForPredict))

def main():
    test()

if __name__ == '__main__':
    main()
