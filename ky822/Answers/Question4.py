'''
Created on Nov 3, 2014

@author: ds-ga-1007
'''
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def Question4():
    """ Compute the Mandelbrot fractal using the Mandelbrot iteration. """
    print '------Question 4------'
    print 'Question 4: Write a module that computes the Mandelbrot fractal using the Mandelbrot iteration'
    
    # a. Constructing a grid of c = x + 1j*y values in range [-2, 1] x [-1.5, 1.5]
    grid_number = 400
    x = np.linspace(-2,1,grid_number)
    y = np.linspace(-1.5,1.5,grid_number)
    c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
    
    # b. Do the iteration
    N_max = 50
    some_threshold = 50
    z = c
    for v in range(N_max):
        z = z**2 + c
    
    # c. Form a 2-D boolean mask indicating which points are in the set
    mask = (abs(z)<some_threshold)
    
    # Save the result to an image 
    plt.imshow(mask.T, extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    
    print '----------------------'
    
if __name__ == '__main__':
    Question4()