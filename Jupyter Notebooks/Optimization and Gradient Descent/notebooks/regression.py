# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:27:05 2022

@author: javier.perez-alvaro
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# LINEAR REGRESSION WITH GRADIENT DESCENT FUNCTION
def linregression_GD(X,y,learning_rate, n_epochs = 100, test_data = None):
    '''
    linear regression with Gradient Descent
    
    INPUT: 
    - the feature matrix X
    - the target vector y
    - learning rate
    - epochs: number of Gradient Descent iterations (default 100)
    - test_data (optional): data (X_test,y_test) for monitoring overfitting
    
    OUTPUT:
    - the vector theta
    - mean squared error at each iteration
    '''
    m,n = X.shape # size of data set, number of features
    theta = np.random.randn(n) # random initialization
    
    # initialize mse vector 
    mse = np.zeros(n_epochs)

    # initialize mse_test vector (if test_data is not None)
    if test_data: 
        X_test,y_test = test_data
        mse_test = np.zeros(n_epochs)
        
    
    
    # gradient descent iterations
    for epoch in range(n_epochs):
        gradient = 2*X.T.dot(X.dot(theta)-y) # gradient 
        theta = theta - learning_rate*gradient # update the vector theta
        # compute mean squared error 
        mse[epoch] = np.mean((y-X.dot(theta))**2)
        # compute test mean squared error
        if test_data:
            mse_test[epoch] = np.mean((y_test-X_test.dot(theta))**2)
            
            
    results = {}
    results['theta'] = theta
    results['mse'] = mse
    if test_data:
        results['mse_test'] = mse_test
    return results

# BUILD POLYNOMIAL FEATURES FUNCTION
def build_poly_features(X,degree):
    from itertools import combinations_with_replacement as comb_w_r
    from itertools import chain
    
    # number of datapoints (rows), number of features (columns)
    try:
        m,n = X.shape # this won't work if X is a vector (n=1 features)
    except: 
        m = len(X)
        n = 1
        X = X.reshape(m,1) #  
    
    # number of polynomial features
    combinations = chain.from_iterable(comb_w_r(range(n),i) for i in range(degree+1))
    n_poly = sum(1 for combination in combinations) 
    
    # polynomial features matrix
    X_poly = np.ones((m,n_poly))
    combinations = chain.from_iterable(comb_w_r(range(n),i) for i in range(degree+1))\
    
    
    for column_index, combination in enumerate(combinations):
        X_poly[:,column_index] = np.prod(X[:,combination],axis=1)
        
    return X_poly