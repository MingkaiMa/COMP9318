import pandas as pd
import numpy as np
import sys

data_file='./asset/a'
raw_data = pd.read_csv(data_file, sep=',')
raw_data.head()

labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)

coefficients = np.zeros(3) # We initialize the coefficients with ZERO. We also compute the intercept term.
num_epochs = 10
learning_rate = 50e-5



def sigmoid(data, coefficients):

    z = np.dot(data, coefficients[1: ]) + coefficients[0]

    return 1.0 / (1.0 + np.exp(-z))




for i in range(num_epochs):

    hx = sigmoid(data, coefficients)

    error = hx - labels

    grad = data.T.dot(error)
    
    coefficients[0] = coefficients[0] - learning_rate * error.sum()
    coefficients[1:] = coefficients[1:] - learning_rate * grad

print(coefficients)
    
