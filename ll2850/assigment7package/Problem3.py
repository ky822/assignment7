__author__ = 'leilu'
'''
Created on Nov 2, 2014

@author: leilu
'''

import numpy as np
from array import *
from numpy import argsort


#print random_matrix

def Find_closest():
    ran_matrix=np.random.rand(10,3)#first generate a random matrix
    total=[]
    for row in range(len(ran_matrix)):
        row_element=ran_matrix[row]
        Diff_Row=[]
        for i in range(len(row_element)):
            diff=np.abs(row_element[i]-0.5)
            Diff_Row.append(diff)

        smallest_i=argsort(Diff_Row)[0]
        closest_num=row_element[smallest_i]
        total.append(closest_num)
    print total
