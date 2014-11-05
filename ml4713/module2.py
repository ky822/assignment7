# -*- coding: utf-8 -*-
"""
Homework 7
Module 2
Mengfei Li
"""

import numpy as np



def program2():
    
    #Creating Array
    a=np.arange(25).reshape(5,5)
    b=np.array([1.,5,10,15,20])
    
    #Initializing an array for final result
    result=np.zeros(shape=(5,5))

    for i in np.arange(a.shape[1]):
        result[:,i]=np.divide(a[:,i],b)
    
    print '-----------Question 2----------'
    print 'The result is: \n', result