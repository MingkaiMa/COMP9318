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

print(clf.score(test_data_matrix, test_label))

dual_coef = clf.dual_coef_[0]

class_0_dual_coef = dual_coef[: clf.n_support_[0]]
class_1_dual_coef = dual_coef[clf.n_support_[0]: ]

support_vector_index = clf.support_

class_0_dual_sv_index = []
class_1_dual_sv_index = []
for i in range(len(dual_coef)):
    if i < clf.n_support_[0]:
        class_0_dual_sv_index.append((dual_coef[i], support_vector_index[i]))
    else:
        class_1_dual_sv_index.append((dual_coef[i], support_vector_index[i]))
        
    
    
class_0_dual_sv_index = sorted(class_0_dual_sv_index,
                               key = lambda x: abs(x[0]), reverse=True)

class_1_dual_sv_index = sorted(class_1_dual_sv_index,
                               key = lambda x: x[0], reverse=True)




for test_instance in test_data_matrix:

    change_count = set()

    for d1 in class_1_dual_sv_index:
        index = d1[1]
        train_instance = train_data_matrix[index]

        for i in range(len(test_instance)):
            if test_instance[i] == 1 and train_instance[i] == 1:
                if i in change_count:
                    continue
                
                test_instance[i] = 0
                change_count.add(i)
                if len(change_count) >= 20:
                    break


        if len(change_count) >= 20:
            break

    if len(change_count) >= 20:
        continue

    for d0 in class_0_dual_sv_index:
        index = d0[1]
        train_instance = train_data_matrix[index]

        for i in range(len(test_instance)):
            if test_instance[i] == 0 and train_instance[i] == 1:
                if i in change_count:
                    continue
                
                test_instance[i] = 1

                if len(change_count) >= 20:
                    break



        if len(change_count) >= 20:
            break


    if len(change_count) >= 20:
        continue



modified_data = 'modified_data.txt'

with open(modified_data, 'a') as f:
    for i in range(len(test)):
        print(i)
        words_in_original = test[i]
        words_in_training = word_list
        words_all = set(words_in_original) | set(words_in_training)
        words_all = sorted(words_all)

        modified_test_instance = test_data_matrix[i]
        
        for word in words_all:
            if word not in words_in_training:
                f.write(f'{word} ')
            else:
                word_index = word_list.index(word)

                if modified_test_instance[word_index] == 0:
                    continue

                f.write(f'{word} ')

        f.write('\n')

                
    
        

    
