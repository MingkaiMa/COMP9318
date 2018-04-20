
class0_file = '../class-0.txt'
class1_file = '../class-1.txt'

class_0 = []
class_1 = []

with open(class0_file) as class0:
    class_0 = [line.strip().split(' ') for line in class0]

with open(class1_file) as class1:
    class_1 = [line.strip().split(' ') for line in class1]
    

class_all = class_0 + class_1

dic_class_0 = {}
vocabulary_0 = set()
wordCount_0 = 0

dic_class_1 = {}
vocabulary_1 = set()
wordCount_1 = 0

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
