from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm

class0_file = '../class-0.txt'
class1_file = '../class-1.txt'
test_file = '../test_data.txt'

class_0 = []
class_1 = []
test = []

with open(class0_file) as class0:
    class_0 = [line.strip().split(' ') for line in class0]

with open(class1_file) as class1:
    class_1 = [line.strip().split(' ') for line in class1]

with open(test_file) as testfile:
    test = [line.strip().split(' ') for line in testfile]
    

class_0 = [' '.join(i) for i in class_0]
class_1 = [' '.join(i) for i in class_1]
test = [' '.join(i) for i in test]

vectorizer = CountVectorizer(lowercase = False,
                            stop_words = None)


##X = vectorizer.fit_transform(class_0 + class_1 + test)

train_data = vectorizer.fit_transform(class_0 + class_1)
tfidf_transformer = TfidfTransformer()
train_data_tfidf = tfidf_transformer.fit_transform(train_data)


test_data = vectorizer.transform(test)
test_data_tfidf = tfidf_transformer.transform(test_data)


##
####
####L = vectorizer.get_feature_names()
####S = set(L)
####
####
y0 = [0] * 360
y1 = [1] * 180
y = y0 + y1
####

clf = svm.SVC()
clf.fit(train_data_tfidf, y)
####
####
##
##
test_label = [1] * 200
####import numpy as np
####print(np.mean())
##
##
#### now it 100%
##clf.score(test_data, test_label)
##
##
##
##
##clf.support_vectors_
##clf.n_support_
##clf.support_
