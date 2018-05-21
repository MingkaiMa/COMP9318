import helper
from sklearn import svm
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score


test_data = 'test_data.txt'
strategy_instance=helper.strategy() 
parameters={'gamma': 'auto',
            'C': 0.020999999999999998,
            'kernel': 'linear',
            'degree': 3,
            'coef0': 0}




test_file = test_data
    
class_0 = strategy_instance.class0
class_1 = strategy_instance.class1
test = []

with open(test_file) as f:
    test = [line.strip().split(' ') for line in f]


class_all = class_0 + class_1

vocabulary = set()

for sentence in class_all:
    for word in sentence:
        vocabulary.add(word)

word_list = sorted(vocabulary)


train_data_matrix = []

for sample in class_all:
    temp_list = []
    for word in word_list:
        if word in sample:
            temp_list.append(1)
        else:
            temp_list.append(0)
    train_data_matrix.append(temp_list)

train_data_matrix = np.array(train_data_matrix)


test_data_matrix = []

for sample in test:
    temp_list = []
    for word in word_list:
        if word in sample:
            temp_list.append(1)
        else:
            temp_list.append(0)

    test_data_matrix.append(temp_list)

test_data_matrix = np.array(test_data_matrix)


train_label = [0] * 360 + [1] * 180
train_label = np.array(train_label)

test_label = [1] * 200
test_label = np.array(test_label)

##clf_start = strategy_instance.train_svm(parameters, train_data_matrix, train_label)
####
##param_range = np.arange(0.001,1,0.01)
##
##param_grid = [{'C': param_range, 'kernel': ['linear']}]
##grid = GridSearchCV(clf_start, param_grid)
##grid.fit(train_data_matrix, train_label)
##clf = grid.best_estimator_
##print(clf)

clf = strategy_instance.train_svm(parameters, train_data_matrix, train_label)

print(cross_val_score(clf, train_data_matrix, train_label))
##clf = strategy_instance.train_svm(parameters, train_data_matrix, train_label)
##


# C = 1
##for c in range(-10, 10):
##    clf = svm.SVC(kernel = 'poly', C = 2 ** c, coef0 = 12, degree = 3, gamma = 0.0001)
##    clf.fit(train_data_matrix, train_label)
##    print(f'C is: {2 ** c}')
##    print(clf.score(train_data_matrix, train_label))
##    print(clf.score(test_data_matrix, test_label))


# coef0 = 2048
##for coef in range(8, 20):
####for coef in range(8, 17):
##    clf = svm.SVC(kernel = 'poly', C = 1, coef0 = 2 ** coef, degree = 3, gamma = 0.0001)
##    clf.fit(train_data_matrix, train_label)
##    print(f'coef0 is: {2 ** coef}')
##    print(clf.score(train_data_matrix, train_label))
##    print(clf.score(test_data_matrix, test_label))


##clf = svm.SVC(kernel = 'poly', C = 1, coef0 = 2048, degree = 3, gamma = 0.0001)
##clf.fit(train_data_matrix, train_label)


# degree = 3
##for deg in range(-10, 10):
##for deg in range(2, 9):
##    clf = svm.SVC(kernel = 'poly', C = 1, coef0 = 2048, degree = deg, gamma = 0.0001)
##    clf.fit(train_data_matrix, train_label)
##    print(f'degree is: {deg}')
##    print(clf.score(train_data_matrix, train_label))
##    print(clf.score(test_data_matrix, test_label))
##
##
## 0.455
##clf = svm.SVC(kernel = 'poly', C = 1, coef0 = 2048, degree = 3, gamma = 0.0001)
##clf.fit(train_data_matrix, train_label)

# gamma = 0.0001
##for ga in range(-10, 10):
##    clf = svm.SVC(kernel = 'poly', C = 1, coef0 = 2048, degree = 3, gamma = 10 ** ga)
##    clf.fit(train_data_matrix, train_label)
##    print(f'gamma is: {10 ** ga}')
##    print(clf.score(train_data_matrix, train_label))
##    print(clf.score(test_data_matrix, test_label))
##    
