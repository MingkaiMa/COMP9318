import helper
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import numpy as np
from sklearn.model_selection import GridSearchCV


test_file = 'test_data.txt'

strategy_instance=helper.strategy()


class_0 = strategy_instance.class0
class_1 = strategy_instance.class1

class_all = class_0 + class_1

class_all = [' '.join(i) for i in class_all]




vectorizer = CountVectorizer(stop_words = None)
vectorizer.fit(class_all)

##print(vectorizer.vocabulary_)


tmp_dic = vectorizer.vocabulary_

word_list = sorted(tmp_dic, key = lambda x: tmp_dic[x])



train_data = vectorizer.transform(class_all).toarray()
train_label = np.array([0] * 360 + [1] * 180)

test = []
with open(test_file) as f:
    for line in f:
        test.append(line)

test_data = vectorizer.transform(test).toarray()
test_label = np.array([1] * 200)


##grid = GridSearchCV(svm.SVC(kernel = 'poly'),
##                    param_grid = {"C": [0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16],
##                                  "degree": [i for i in range(1, 20)],
##                                  "coef0": [0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16]},
##                    n_jobs = 4,
##                    cv = 10)
##
##
##grid.fit(train_data, train_label)
##print(grid.best_params_, grid.best_score_)

## Select best parameters:
clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = 3, gamma = 0.0001)
clf.fit(train_data, train_label)




