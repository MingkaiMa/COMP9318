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
num_epochs = 5
learning_rate = 50e-5





def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

for i in range(num_epochs):
    loss = labels - sigmoid(np.dot(data, coefficients))

    coefficients = coefficients + learning_rate * data.transpose() * loss
    i += 1

print(coefficients)
