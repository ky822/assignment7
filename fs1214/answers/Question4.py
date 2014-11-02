'''
Created on Oct 30, 2014

@author: ds-ga-1007
'''

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def main():
    print '-----Question4-----'
    #define constant.
    N_max = 50
    some_threshold = 50
    
    #construct a grid of x,y in range [-2, 1], [-1.5, 1.5].
    num_x = 500
    num_y = 500
    x = np.linspace(-2,1,num_x)
    y = np.linspace(-1.5,1.5,num_y)
    c = x[:,newaxis]+1j*y[newaxis,:]
    
    #do the iteration
    z = c
    for v in range(N_max):
        z = z**2 + c
    
    #define the boolean mask.
    mask = abs(z) < some_threshold
    
    #draw the image and save the result
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    
    print '----------------'
if __name__ == '__main__':
    main()