# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:14:02 2014

@author: peter
"""

import numpy as np

print 'Question 3', '\n'

# Generate Random Matrix
aa = np.random.rand(10,3)

# compute the distance of each element from 0.5
distAA =  abs(aa - 0.5)

# Find Index of Minimum Element
minElement = np.argmin(distAA,1)
idxMin = zip(np.arange(10),minElement)

# Print closest element to 0.5
print [aa[i] for i in idxMin]