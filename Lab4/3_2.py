import pandas as pd
import numpy as np
import sys

data_file='./asset/a'
raw_data = pd.read_csv(data_file, sep=',')
raw_data.head()

labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)

one = np.ones((data.shape[0], 1), dtype='float64')
data = np.append(one, data, axis = 1)

coefficients = np.zeros(3) # We initialize the coefficients with ZERO. We also compute the intercept term.
num_epochs = 1
learning_rate = 50e-5




def w_x(data, coefficients):
##    res = 0
##    for i in range(len(coefficients)):
##        res += coefficients[i] * data[i]

    return np.dot(data, coefficients)

def sigmoid_func(array):

    s = sum(array)

    res = np.exp(s) / (1 + np.exp(s))
    return res

for count in range(num_epochs):

    print(count)


    sigmoid = data * coefficients

    sigmoid_ = np.apply_along_axis(sigmoid_func, 1, sigmoid)

    print(sigmoid_)
    error = labels - sigmoid_

    grad = data.T.dot(error)

    print(grad)
    coefficients = coefficients + learning_rate * grad
    sys.exit()
##    for i in range(len(coefficients)):
##
##        w = 0
##        
##        for j in range(len(data)):
##
##            w += data[j][i] * (labels[j] - sigmoid_[j])
##
##        coefficients[i] += learning_rate * w
##    

    count += 1


print(coefficients)
