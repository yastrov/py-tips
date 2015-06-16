# -*- coding: utf-8 -*-
from __future__ import division, print_function
from codecs import open as copen
from collections import defaultdict
from math import log

__doc__ = """Rewrite example from http://habrahabr.ru/post/120194/
by Yuriy Astrov

Now work...:
For each word create vector with features
Store vector in dictionary

I think that one vector of word feature is better than
dictionary without deterministic structure (many existing or not existing keya)
and with problem with conversion beyond dictionary and string representation.

(Я счёл, что хранить в словаре свойства, преобразованные в вектор лучше, чем хранить преобразованный словарь,
    как это делал автор статьи. Так же сделал рефакторинг, который считаю лучшим для универсальности применения
    и для читаемости *а так же понимания* кода.)

Using fooV and make_vectorV
Or
foo and make_vector

Example of file with words:
cat names.txt
Оксана f
Альберт m
Лазарь m
Христоф m
Рунар m
"""

def foo(x, fil='0'):
    """
    "AbF" -> ['A00', '0b0', '00F']
    """
    assert isinstance(x, (str, unicode))
    l = [c for c in x]
    r = []
    for i in xrange(len(x)):
        p = [fil]* len(x)
        p[i]=l[i]
        r.append(''.join(p))
    return r

def fooV(x, fil='0'):
    """
    ['A', 'b', 'F'] -> [['A', '0', '0'], ['0', 'b', '0'], ['0', '0', 'F']]
    """
    assert isinstance(x, (list, tuple))
    r = []
    for i in xrange(len(x)):
        p = [fil]* len(x)
        p[i]=x[i]
        r.append(tuple(p))
    return r


class NaiveBayes(object):
    def __init__(self, separateVector=fooV):
        self.reset()
        self._separateVector = separateVector

    def reset(self):
        """Reset to INIT state"""
        self._classes = defaultdict(lambda:0)
        self._freq = defaultdict(lambda:0)
        
    def train(self, samples):
        assert isinstance(samples, (list, tuple))
        classes, freq = self._classes, self._freq
        separateVector = self._separateVector
        for vector, label in samples:
            classes[label] += 1                 # count classes frequencies
            for feat in separateVector(vector):
                freq[label, feat] += 1          # count features frequencies

        for label, feat in freq:                # normalize features frequencies
            freq[label, feat] /= classes[label]
        for c in classes:                       # normalize classes frequencies
            classes[c] /= len(samples)
        #return classes, freq              # return P(C) and P(O|C)

    def classify(self, VectorOfFeat):
        """Classify one object via their vector of feature"""
        assert isinstance(VectorOfFeat, (list, tuple, str, unicode))
        classes, prob = self._classes, self._freq
        separateVector = self._separateVector
        return min(classes.keys(),              # calculate argmin(-log(C|O))
                    key = lambda label: -log(classes[label]) + \
                        sum(
                            -log(prob.get((label,feat), 10**(-7)))
                            for feat in separateVector(VectorOfFeat)
                            )
                   )


def test(classifier, test_set):
    assert isinstance(classifier, NaiveBayes)
    assert isinstance(test_set, (list, tuple))
    hits = 0
    for vectorOfFeat, label, name in test_set:
        if label == classifier.classify(vectorOfFeat):
            hits += 1
        else:
            print("Error!", name,
                  ''.join((vectorOfFeat[2], vectorOfFeat[1],'.+?', vectorOfFeat[0])),
                  label)
    return hits/len(test_set)

def make_vector(sample):
    """
    last letter, first letter, second letter
    """
    return ''.join((sample[-1], sample[1], sample[0]))

def make_vectorV(sample):
    """
    last letter, first letter, second letter
    """
    return (sample[-1], sample[1], sample[0])

def main():
    samples = None
    with copen('names.txt', 'r', encoding="UTF-8") as f:
        samples = tuple(line.rstrip().split() for line in f)
    features = [(make_vectorV(feat), label, feat) for feat, label in samples]
    train_set, test_set = features[:-100], features[-100:]
    classifier = NaiveBayes(fooV)
    classifier.train( [(x[0], x[1]) for x in train_set] )
    print('Accuracy: ', test(classifier, test_set))

if __name__ == '__main__':
    main()
