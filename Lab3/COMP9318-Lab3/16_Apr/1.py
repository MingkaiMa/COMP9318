import pandas as pd

raw_data = pd.read_csv('../asset/data.txt', sep = '\t')

def tokenize(sms):
    return sms.split(' ')

def get_freq_of_tokens(sms):
    tokens = {}
    for token in tokenize(sms):
        if token not in tokens:
            tokens[token] = 1
        else:
            tokens[token] += 1

    return tokens

training_data = []
for index in range(len(raw_data)):
    training_data.append((get_freq_of_tokens(raw_data.iloc[index].text), raw_data.iloc[index].category))


##def multinomial_nb(training_data, sms):# do not change the heading of the function

total_instances = len(training_data)
class_prior_dic = {}
for i in training_data:
    if i[1] not in class_prior_dic:
        class_prior_dic[i[1]] = 1
    else:
        class_prior_dic[i[1]] += 1



vocabulary = set()
totalWordsHam = 0
totalWordsSpam = 0

for i in training_data:
    if i[1] == 'ham':
        for j in i[0]:
            totalWordsHam += i[0][j]
            vocabulary.add(j)

    else:
        for j in i[0]:
            totalWordsSpam += i[0][j]
            vocabulary.add(j)

dic_total = {'spam': totalWordsSpam, 'ham':totalWordsHam}
            

dic = {}

for i in training_data:
    if i[1] not in dic:
        dic[i[1]] = {}


for i in training_data:

    for j in i[0]:
        if j not in dic[i[1]]:
            dic[i[1]][j] = i[0][j]

        else:
            dic[i[1]][j] += i[0][j]
        


# sms = 'Chinese Chinese Chinese Tokyo Japan'
sms = 'I am not spam'
wordList = sms.split(' ')

dic_result = {}
for i in training_data:
    if i[1] not in dic_result:
        dic_result[i[1]] = {}

##calculate spam:
for word in wordList:
    if word not in dic['ham']:
        dic_result['ham'][word] = 0 + 1
    else:
        dic_result['ham'][word] = dic['ham'][word] + 1


    if word not in dic['spam']:
        dic_result['spam'][word] = 0 + 1
    else:
        dic_result['spam'][word] = dic['spam'][word] + 1
        
            

ham_resultList = 1
spam_resultList = 1

for word in wordList:
    print(word)
    ham_resultList *= dic_result['ham'][word] / (dic_total['ham'] + len(vocabulary))
    spam_resultList *= dic_result['spam'][word] / (dic_total['spam'] + len(vocabulary))


ham_resultList *= (class_prior_dic['ham'] + 1)/ (class_prior_dic['ham'] + class_prior_dic['spam'] + 2)
spam_resultList *= (class_prior_dic['spam'] + 1)/ (class_prior_dic['ham'] + class_prior_dic['spam'] + 2)


##log
from math import log

ham_resultListLog = 0
spam_resultListLog = 0

for word in wordList:
    ham_resultListLog += log(dic_result['ham'][word] / (dic_total['ham'] + len(vocabulary)))
    spam_resultListLog += log(dic_result['spam'][word] / (dic_total['spam'] + len(vocabulary)))

ham_resultListLog += log(class_prior_dic['ham'] / (class_prior_dic['ham'] + class_prior_dic['spam']))
spam_resultListLog += log(class_prior_dic['spam'] / (class_prior_dic['ham'] + class_prior_dic['spam']))
