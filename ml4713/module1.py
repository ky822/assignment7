# -*- coding: utf-8 -*-
"""
Homework 7
Module 1
Mengfei Li
"""

import numpy as np


def program1():
    
    
  
    #Create the required array
    newArray=np.arange(1,16).reshape((5,3),order='F')
    #part a
    a_Array=newArray[[1,3],:]
    #part b
    b_Array=newArray[:,1]
    #part c
    c_Array=newArray[1:4,0:3]
    #part d   
    d_Array=np.array([],dtype=int)
    for i,j in zip(np.where((newArray>=3)&(newArray<=11))[0],np.where((newArray>=3)&(newArray<=11))[1]):
        d_Array=np.append(d_Array,newArray[i][j])

    print '-----------Question 1----------'
    print 'Part a: \n', a_Array
    print 'Part b: \n', b_Array
    print 'Part c: \n', c_Array
    print 'Part d: \n', d_Array
