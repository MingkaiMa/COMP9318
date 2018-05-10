import submission as submission
import pandas as pd
import numpy as np
## Read in the Data...
data_file='./asset/a'
raw_data = pd.read_csv(data_file, sep=',')
labels=raw_data['Label'].values
data=np.stack((raw_data['Col1'].values,raw_data['Col2'].values), axis=-1)

## Fixed Parameters. Please do not change values of these parameters...
coefficients = np.zeros(3) # We initialize the coefficients with ZERO. We also compute the intercept term.
num_epochs = 10
learning_rate = 50e-5



coefficients=submission.logistic_regression(data, labels, coefficients, num_epochs, learning_rate)
print(coefficients)
