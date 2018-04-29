import helper
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


    test_data_matrix = []
    for sample in test:
        temp_list = []
        for word in word_list_class_0_1:
            temp_list.append(sample.count(word))
        test_data_matrix.append(temp_list)

    print(len(test_data_matrix), '   ', len(test_data_matrix[0]))
    test_data_matrix = np.array(test_data_matrix)


    y_train = [0] * 360 + [1] * 180
    y_train = np.array(y_train)

    y_test = [1] * 200
    y_test = np.array(y_test)
##    clf = svm.SVC(kernel = 'poly', C = 10 ** 2, coef0 = 12, degree = 3, gamma = 0.0001)

    clf = strategy_instance.train_svm(parameters, train_data_matrix, y_train)
    
    print(clf.score(train_data_matrix, y_train))
    print(clf.score(test_data_matrix, y_test))


    support_vector_for_class_0 = 


    

    

##    ##..................................#
##    #
##    #
##    #
##    ## Your implementation goes here....#
##    #
##    #
##    #
##    ##..................................#
##    
##    
##    ## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...
##    
##    
##    ## You can check that the modified text is within the modification limits.
##    modified_data='./modified_data.txt'
##    assert strategy_instance.check_data(test_data, modified_data)
##    return strategy_instance ## NOTE: You are required to return the instance of this class.
