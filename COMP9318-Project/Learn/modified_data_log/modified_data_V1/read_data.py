from sklearn import svm
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import sys

class0_file = '../class-0.txt'
class1_file = '../class-1.txt'
test_file = '../test_data.txt'

##class0_file = '../mydata/0.txt'
##class1_file = '../mydata/1.txt'
##test_file = '../mydata/test.txt'

class_0 = []
class_1 = []
test = []

with open(class0_file) as class0:
    class_0 = [line.strip().split(' ') for line in class0]

with open(class1_file) as class1:
    class_1 = [line.strip().split(' ') for line in class1]
    

with open(test_file) as testFile:
    test = [line.strip().split(' ') for line in testFile]

class_all = class_0 + class_1

dic_class_0 = {}
vocabulary_0 = set()
wordCount_0 = 0

dic_class_1 = {}
vocabulary_1 = set()
wordCount_1 = 0

dic_class_0_1 = {}

dic_test = {}
vocabulary_test = set()
wordCountTest = 0

for sentence in class_0:
    for word in sentence:
        wordCount_0 += 1
        vocabulary_0.add(word)
        if word not in dic_class_0:
            dic_class_0[word] = 1
        else:
            dic_class_0[word] += 1
    


for sentence in class_1:
    for word in sentence:
        wordCount_1 += 1
        vocabulary_1.add(word)
        if word not in dic_class_1:
            dic_class_1[word] = 1
        else:
            dic_class_1[word] += 1


vocabulary_all = set()
for sentence in class_all:
    for word in sentence:
        vocabulary_all.add(word)
        if word not in dic_class_0_1:
            dic_class_0_1[word] = 1
        else:
            dic_class_0_1[word] += 1

for sentence in test:
    for word in sentence:
        wordCountTest += 1
        vocabulary_test.add(word)
        if word not in dic_test:
            dic_test[word] = 1
        else:
            dic_test[word] += 1


word_list_class_0 = []
for word in dic_class_0:
    word_list_class_0.append(word)
    

word_list_class_1 = []
for word in dic_class_1:
    word_list_class_1.append(word)


word_list_class_0_1 = []
for word in dic_class_0_1:
    word_list_class_0_1.append(word)

train_data_matrix = []

for sample in class_all:
    temp_list = []
    for word in word_list_class_0_1:
        temp_list.append(sample.count(word))
    train_data_matrix.append(temp_list)

train_data_matrix = np.array(train_data_matrix)

train_data_matrix_class_0 = []
for sample in class_0:
    temp_list = []
    for word in word_list_class_0:
        temp_list.append(sample.count(word))
    train_data_matrix_class_0.append(temp_list)



train_data_mtraix_class_1 = []
for sample in class_1:
    temp_list = []
    for word in word_list_class_1:
        temp_list.append(sample.count(word))
    train_data_mtraix_class_1.append(temp_list)


test_data_matrix = []
for sample in test:
    temp_list = []
    for word in word_list_class_0_1:
        temp_list.append(sample.count(word))
    test_data_matrix.append(temp_list)

test_data_matrix = np.array(test_data_matrix)


y_train = [0] * 360 + [1] * 180
y_train = np.array(y_train)
##y_train_class_0 = [0] * 360
###y_train = [0] * 3 + [1] * 3
##clf = svm.SVC(kernel = 'linear', C = 200)
##clf.fit(train_data_matrix, y_train)

y_test = [1] * 200
y_test = np.array(y_test)

## Select best parameters:
clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = 3, gamma = 0.0001)
clf.fit(train_data_matrix, y_train)

sv_index_class_0 = clf.n_support_[0]
sv_index_class_1 = clf.n_support_[1]


support_vectors_for_class_0 = clf.support_vectors_[ :sv_index_class_0]
support_vectors_index_for_class_0 = clf.support_[ :sv_index_class_0]


support_vectors_for_class_1 = clf.support_vectors_[sv_index_class_0: ]
support_vectors_index_for_class_1 = clf.support_[sv_index_class_0: ]


for test_instance in test_data_matrix:
    test_distance_to_class_0_sv = euclidean_distances([test_instance], support_vectors_for_class_0)
    #print(np.min(test_distance_to_class_0_sv))
    
    #print(np.argmin(test_distance_to_class_0_sv))
    min_index = np.argmin(test_distance_to_class_0_sv)
    target_train_instance_index = support_vectors_index_for_class_0[min_index]
    target_train_instance = train_data_matrix[target_train_instance_index]

    #print(clf.decision_function([target_train_instance]))
    #print(clf.decision_function([clf.support_vectors_[min_index]]))

    #sys.exit()

    change_count = 0
    
    for i in range(len(test_instance)):
        if change_count > 20:
            break
        
        if test_instance[i] != target_train_instance[i]:

            # save previous decision distance
            previous_dd = clf.decision_function([test_instance])
            
            #
            # save test_instance[i]
            

            save_value = test_instance[i]


            if test_instance[i] < target_train_instance[i]:
                to_add_value = min(20 - change_count, target_train_instance[i] - test_instance[i])
                test_instance[i] += to_add_value

            else:
                to_add_value = min(20 - change_count, test_instance[i] - target_train_instance[i])
                test_instance[i] -= to_add_value

            now_dd = clf.decision_function([test_instance])

            # decrease the dd
            if now_dd < previous_dd:
                change_count += to_add_value
                continue

            else:
                test_instance[i] = save_value
            
                

            

print(clf.score(test_data_matrix, y_test))


modified_data = 'modified_data.txt'

with open(modified_data, 'a') as f:
    for modified_test_instance in test_data_matrix:
        for i in range(len(modified_test_instance)):
            if modified_test_instance[i] == 0:
                continue

            f.write(f'{word_list_class_0_1[i]} ' * modified_test_instance[i])

        f.write('\n')
    
    









##    print()
##    
##    print()
##    break


## coef0 = 12
##for c in range(1,20):
##    clf = svm.SVC(kernel = 'poly', coef0 = c)
##    clf.fit(train_data_matrix, y_train)
##
##    print('train: ', clf.score(train_data_matrix, y_train))
##
##    print('test:  ', clf.score(test_data_matrix,  y_test))


##C parameter
## C = 10 ** 2
##for c in range(-5, 15):
##    clf = svm.SVC(kernel = 'poly', C = 2 ** c, coef0 = 12)
##    clf.fit(train_data_matrix, y_train)
##    print(f'c is: {c} C is : {2 ** c}')
##    print('train: ', clf.score(train_data_matrix, y_train))
##    print('test:  ', clf.score(test_data_matrix,  y_test))
##

##degree parameter
## best between degree = 2,3,4
## after 5 , decrease

##for d in range(1, 30):
##    clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = d)
##    clf.fit(train_data_matrix, y_train)
##
##    print(f'degree is {d}')
##    print('train: ', clf.score(train_data_matrix, y_train))
##    print('test:  ', clf.score(test_data_matrix,  y_test))


##degree gamma
## gamma best between: 0.0001

##ini = 0.00017488632388947185
##g__L = [i * (-0.00001) + ini for i in range(1, 15)]
##g_L = [i * 0.0001 + ini for i in range(1, 15)]
##gL = g__L + g_L
##
##for g in range(-15, 5):
##    
##    clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = 3, gamma = 2 ** g)
##    clf.fit(train_data_matrix, y_train)
##    print('train: ', clf.score(train_data_matrix, y_train))
##    print('test:  ', clf.score(test_data_matrix,  y_test))
##    print()




##sv_class_0 = clf.n_support_[0]
##sv_class_1 = clf.n_support_[1]
##
##support_vector_for_class_0 = clf.support_vectors_[: sv_class_0]
##support_vector_for_class_1 = clf.support_vectors_[sv_class_0: ]
##
##for instance in test_data_matrix:
##    minDistance = float('inf')
##    minInstance = []
##    for class0instance in support_vector_for_class_0:
##        distance = euclidean_distances([instance], [class0instance])
##        if(distance > minDistance):
##            minDistance = distance
##            minInstance = class0instance

    
        
    
    





##print(clf)
##
###clf.fit(train_data_matrix, y_train)
##
###clf.fit(train_data_matrix_class_0, y_train_class_0)

