# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:13:50 2014

@author: peter
"""

import matplotlib.pyplot as plt
import numpy as np

print 'Question 4', '\n'

threshold = 50
n_max = 50
grid = 0.01
xRange = np.arange(-2, 1, grid)
yRange = np.arange(-1.5, 1.5, grid)

mapMatrix = np.zeros((xRange.size, yRange.size))

m = 0
n = 0

for x in xRange:
    
    n = 0
    
    for y in yRange:

        c = x + (1j* y)
        z = c

        for v in range(n_max):

            z = z**2 + c

        if abs(z) < threshold:
            
            mapMatrix[m,n] = True
            
        else:
            
            mapMatrix[m,n] = False        
        n+=1
    m+=1
    
plt.imshow(mapMatrix.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')