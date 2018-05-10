import pandas as pd
import numpy as np

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function

    one = np.ones((data.shape[0], 1), dtype='float64')
    data = np.append(one, data, axis = 1)
    coefficients = weights

    for i in range(num_epochs):

        dot_res = np.dot(data, coefficients)
        hx = 1 / (1 + np.exp(-dot_res))
        error = labels - hx 

        g = data.T.dot(error)

        coefficients = coefficients + learning_rate * g


    return coefficients

    

    
    



    
