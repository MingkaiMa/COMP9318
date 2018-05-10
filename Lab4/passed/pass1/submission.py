import pandas as pd
import numpy as np

def sigmoid(data, coefficients):
    z = np.dot(data, coefficients[1: ]) + coefficients[0]
    return 1.0 / (1.0 + np.exp(-z))


def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function


    coefficients = weights

    for i in range(num_epochs):

        hx = sigmoid(data, coefficients)

        error = hx - labels

        grad = data.T.dot(error)
        
        coefficients[0] = coefficients[0] - learning_rate * error.sum()
        coefficients[1:] = coefficients[1:] - learning_rate * grad


    return coefficients

    

    
    



    
