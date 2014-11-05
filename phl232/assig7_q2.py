# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:13:35 2014

@author: peter
"""

import numpy as np

print 'Question 2', '\n'

f = np.arange(25).reshape(5, 5)
g = np.array([1., 5, 10, 15, 20])

# divide f by g column-wise
h = f / g.repeat(5).reshape(5,5) 

print h
