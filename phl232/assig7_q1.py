# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:13:12 2014

@author: peter
"""

import numpy as np

print 'Question 1', '\n'

# Create Initial Array
a = np.arange(1,16).reshape(3,5).T

print a, '\n'

# Generate a new array contain the 2nd and 4th rows.
b = a[(1,3),:]

print b, '\n'

# Generate a new array that contains the 2nd column

c = a[:,1]

print c, '\n'

# Generate a new array that contains all the elements in the rectangular section between
# the coordinates [1,0] to [3,2]

d = a[1:4,:]

print d, '\n'

# Generate a new array that contains only elements who’s values are between 3 and 11

e = a[((a>3)*(a<11))]

print e, '\n'