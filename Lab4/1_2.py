import pandas as pd
import numpy as np


data_file='./asset/a'
raw_data = pd.read_csv(data_file, sep=',')
raw_data.head()

labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)

one = np.ones((data.shape[0], 1), dtype='float64')
data = np.append(data, one, axis = 1)

coefficients = np.zeros(3) # We initialize the coefficients with ZERO. We also compute the intercept term.
num_epochs = 5
learning_rate = 50e-5




def w_x(data, coefficients):
##    res = 0
##    for i in range(len(coefficients)):
##        res += coefficients[i] * data[i]

    return np.dot(data, coefficients)

def sigmoid(data, coefficients):
    
    wx = w_x(data, coefficients)
    res = np.exp(wx) / (1 + np.exp(wx))
    return res



for count in range(num_epochs):

    print(count)
    s = 0

    ori_co = coefficients

    for i in range(len(ori_co)):

        w = 0

        for j in range(len(data)):
##            print(i,'  ', j)
            w += data[j][i] * (labels[j] - sigmoid(data[j], ori_co))

        coefficients[i] += w * learning_rate

    count += 1


print(coefficients)
