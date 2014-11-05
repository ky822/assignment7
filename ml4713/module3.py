# -*- coding: utf-8 -*-
"""
Homework 7
Module 3
Mengfei Li
"""
import numpy as np


def program3():
    #Create new array
    newArray=np.random.random((10,3))
    #calculate abs of elements in newArray
    newtmp=map(lambda x: abs(x-0.5),newArray)
    newtmp=np.concatenate(newtmp).reshape(10,3)
    
    #pick out the col number of min value of abs(x-0.5)
    colnum=np.argsort(newtmp)[:,0]
    rownum=np.arange(10)


    print '-----------Question 3----------'
    print 'Result: \n',newArray[rownum,colnum]
