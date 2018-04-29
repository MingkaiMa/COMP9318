import helper
from sklearn import svm
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

def fool_classifier(test_data): ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    
    
    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance=helper.strategy() 
    parameters={'gamma': 0.0001,
                'C': 10 ** 2,
                'kernel': 'poly',
                'degree': 3,
                'coef0': 12}

    test_file = test_data

    class_0 = strategy_instance.class0
    class_1 = strategy_instance.class1
    test = []

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


    word_list_test = []
    for word in dic_test:
        word_list_test.append(word)
        

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


    y_test = [1] * 200
    y_test = np.array(y_test)

    ## Select best parameters:
    
    #clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = 3, gamma = 0.0001)
    clf = strategy_instance.train_svm(parameters, train_data_matrix, y_train)
    #clf.fit(train_data_matrix, y_train)

    sv_index_class_0 = clf.n_support_[0]
    sv_index_class_1 = clf.n_support_[1]


    support_vectors_for_class_0 = clf.support_vectors_[ :sv_index_class_0]
    support_vectors_index_for_class_0 = clf.support_[ :sv_index_class_0]


    support_vectors_for_class_1 = clf.support_vectors_[sv_index_class_0: ]
    support_vectors_index_for_class_1 = clf.support_[sv_index_class_0: ]


    for test_instance in test_data_matrix:
        test_distance_to_class_0_sv = euclidean_distances([test_instance], support_vectors_for_class_0)
        test_distance_to_class_1_sv = euclidean_distances([test_instance], support_vectors_for_class_1)

        min_index = np.argmin(test_distance_to_class_0_sv)
        target_train_instance_index = support_vectors_index_for_class_0[min_index]
        target_train_instance = train_data_matrix[target_train_instance_index]



        min_index2 = np.argmin(test_distance_to_class_1_sv)
        target_train_instance_index_2 = support_vectors_index_for_class_1[min_index2]
        target_train_instance_2 = train_data_matrix[target_train_instance_index_2]



        change_count = 0
        
        for i in range(len(test_instance)):

            if change_count == 20:
                break

            
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





    ##    print(change_count)
    ##    break
                
                    

                
    words_in_test_not_in_train = set(word_list_test) - set(word_list_class_0_1)



    modified_data = 'modified_data.txt'

    ##with open(modified_data, 'a') as f:
    ##    for word in words_in_test_not_in_train:
    ##        f.write(f'{word}: ')
    ##    for modified_test_instance in test_data_matrix:
    ##        for i in range(len(modified_test_instance)):
    ##            if modified_test_instance[i] == 0:
    ##                continue
    ##
    ##            f.write(f'{word_list_class_0_1[i]} ' * modified_test_instance[i])
    ##
    ##        f.write('\n')
        
        
    with open(modified_data, 'a') as f:
        for i in range(len(test)):
            words_in_original = test[i]
            words_in_training = word_list_class_0_1
            words_all = set(words_in_original) | set(words_in_training)
            
            modified_test_instance = test_data_matrix[i]

            for word in words_all:
                if word not in words_in_training:
                    f.write(f'{word} ')
                else:
                    word_index = word_list_class_0_1.index(word)

                    if modified_test_instance[word_index] == 0:
                        continue

                    f.write(f'{word} ' * modified_test_instance[word_index])

            f.write('\n')

        


    

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

    return strategy_instance ## NOTE: You are required to return the instance of this class.



fool_classifier('test_data.txt')
