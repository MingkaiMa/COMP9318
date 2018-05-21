import helper
from sklearn import svm
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import sys
from sklearn.feature_extraction.text import CountVectorizer

test_data = 'test_data.txt'
##def fool_classifier(test_data): ## Please do not change the function defination...
##    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
##    
    
    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
strategy_instance=helper.strategy() 
parameters={'gamma': 0.0001,
            'C': 10 ** 2,
            'kernel': 'poly',
            'degree': 3,
            'coef0': 12}

test_file = test_data


class_0 = [' '.join(i) for i in strategy_instance.class0]
class_1 = [' '.join(i) for i in strategy_instance.class1]

with open(test_file) as testFile:
    test=[line.strip().split(' ') for line in testFile]


test = [' '.join(i) for i in test]

class_all = class_0 + class_1



vectorizer = CountVectorizer(min_df=1, token_pattern='(?u)\\b\\w+\\b',
                             stop_words = None)

vectorizer.fit(class_all)



train_data_matrix = vectorizer.transform(class_all).toarray()

test_data_matrix = vectorizer.transform(test).toarray()

word_list_class_0_1 = vectorizer.get_feature_names()


y_train = [0] * 360 + [1] * 180
y_train = np.array(y_train)


y_test = [1] * 200
y_test = np.array(y_test)




## Select best parameters:

#clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = 3, gamma = 0.0001)
clf = strategy_instance.train_svm(parameters, train_data_matrix, y_train)
clf.fit(train_data_matrix, y_train)



sv_index_class_0 = clf.n_support_[0]
sv_index_class_1 = clf.n_support_[1]


support_vectors_for_class_0 = clf.support_vectors_[ :sv_index_class_0]
support_vectors_index_for_class_0 = clf.support_[ :sv_index_class_0]


support_vectors_for_class_1 = clf.support_vectors_[sv_index_class_0: ]
support_vectors_index_for_class_1 = clf.support_[sv_index_class_0: ]


for test_instance in test_data_matrix:
    test_distance_to_class_0_sv = euclidean_distances([test_instance], support_vectors_for_class_0)

    min_index = np.argmin(test_distance_to_class_0_sv)
    target_train_instance_index = support_vectors_index_for_class_0[min_index]
    target_train_instance = train_data_matrix[target_train_instance_index]


    diff = abs(target_train_instance - test_instance)
    L = []
    for i in range(len(diff)):
        L.append((i, diff[i]))



    L = sorted(L, key = lambda x: x[1], reverse=True)

    print(L[: 10])

    change_count = 0
    
    for index in L:
##        print(f'change count: {change_count}')
        i = index[0]

        if(change_count != 20):
            print(f'change count: {change_count}')
        if change_count == 20:


            if test_instance[i] != 0 and target_train_instance[i] != 0:
                #
                # previous value and decision distance
                save_value = test_instance[i]
                previous_dd = clf.decision_function([test_instance])
                
                # now change
                test_instance[i] = target_train_instance[i]

                # compare

                now_dd = clf.decision_function([test_instance])

                if now_dd < previous_dd:
                    continue

                else:
                    test_instance[i] = save_value
            
            continue

        
        if test_instance[i] != target_train_instance[i]:


            # not a modification
            if test_instance[i] != 0 and target_train_instance[i] != 0:
                #
                # previous value and decision distance
                save_value = test_instance[i]
                previous_dd = clf.decision_function([test_instance])
                
                # now change
                test_instance[i] = target_train_instance[i]

                # compare

                now_dd = clf.decision_function([test_instance])

                if now_dd < previous_dd:
                    continue

                else:
                    test_instance[i] = save_value

            #
            # deletion
            elif test_instance[i] != 0 and target_train_instance[i] == 0:
                #
                # previous value and decision distance
                save_value = test_instance[i]
                previous_dd = clf.decision_function([test_instance])

                # now change
                test_instance[i] = 0

                # compare
                now_dd = clf.decision_function([test_instance])

                if now_dd < previous_dd:
                    change_count += 1
    
                    continue
                else:
                    test_instance[i] = save_value

            #
            # addition
            elif test_instance[i] == 0 and target_train_instance[i] != 0:
                #
                # previous value and decision distance
                save_value = test_instance[i]
                previous_dd = clf.decision_function([test_instance])

                # now change
                test_instance[i] = target_train_instance[i]

                # compare
                now_dd = clf.decision_function([test_instance])

                if now_dd < previous_dd:
                    change_count += 1
 
                    continue
                else:
                    test_instance[i] = save_value

            #
            # no modification
            elif test_instance[i] == 0 and target_train_instance[i] == 0:
                continue


    sys.exit()
    



##    print(change_count)
##    break
            


modified_data = 'modified_data.txt'
    
with open(modified_data, 'a') as f:
    for i in range(len(test)):
        words_in_original = test[i].split(' ')
        
##        words_in_training = word_list_class_0_1
##        words_all = set(words_in_original) | set(words_in_training)
##        words_all = sorted(words_all)
##        
##        modified_test_instance = test_data_matrix[i]
##
##        for word in words_all:
##            if word not in words_in_training:
##                f.write(f'{word} ')
##            else:
##                word_index = word_list_class_0_1.index(word)
##
##                if modified_test_instance[word_index] == 0:
##                    continue
##
##                f.write(f'{word} ' * modified_test_instance[word_index])
##
##        f.write('\n')

    




##..................................#
#
#
#
## Your implementation goes here....#
#
#
#
##..................................#


## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...


## You can check that the modified text is within the modification limits.
modified_data='./modified_data.txt'
assert strategy_instance.check_data(test_data, modified_data)

print('all good')
##    return strategy_instance ## NOTE: You are required to return the instance of this class.

