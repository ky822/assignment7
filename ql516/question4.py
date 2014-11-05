# -*- coding: utf-8 -*-

import numpy as np

def construct_a_grid():
    """
    construct a grid of c = x + 1j*y values in range [-2,1] x [-1.5,1.5]
    
    Return
    ======
    an m x n numpy array
    
    """
    grid_number = 100
    x = np.linspace(-2,1,grid_number)
    y = np.linspace(-1.5,1.5,grid_number)
    
    c = []
    
    for i in range(grid_number):
        row = []
        for j in range(grid_number):
            C_element = x[i]+1j*y[j]
            row.append(C_element)
        c.append(row)
    c = np.array(c)
    return c
    

def do_iteration(c):
    """
    Do the Mandelbrot iteration
    
    Argument
    ========
    the grid array C
    
    Return
    ======
    array : the result of the iteration
    """
    N_max = 50
    
    z = np.copy(c)
    
    for v in range(N_max):
        z = z**2+c
    
    return z
    

def generate_mask_array(z):
    """
    return a boolean matrix mask indicating which points are in the set
    """
    some_threshold = 50
    mask = abs(z) < some_threshold
    return np.array(mask)
    
def MandelbrotPlot(mask):
    """
    plot the image of the points in the set and save it
    """
    import matplotlib.pyplot as plt
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    
def mandelbrot():
    """
    the main function to generate a mandelbrot plot
    """
    c = construct_a_grid()
    z = do_iteration(c)
    mask = generate_mask_array(z)
    MandelbrotPlot(mask)
    print "The mandelbrot image has been saved in the working directory"
    
    
if __name__ == "__main__":
    mandelbrot()
    

    