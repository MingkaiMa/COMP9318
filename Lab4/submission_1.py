import pandas as pd
import numpy as np

def sigmoid_func(array):

    s = sum(array)

    res = np.exp(s) / (1 + np.exp(s))
    return res

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function

    one = np.ones((data.shape[0], 1), dtype='float64')
    data = np.append(one, data, axis = 1)
    coefficients = weights

    for count in range(num_epochs):


        sigmoid = data * coefficients

        sigmoid_ = np.apply_along_axis(sigmoid_func, 1, sigmoid)


        error = labels - sigmoid_

        grad = data.T.dot(error)

        coefficients = coefficients + learning_rate * grad
        
        count += 1


    return coefficients

    

    
    



    
