import numpy as np
import matplotlib.pyplot as plt
import itertools 


''' granularity of the grid, if not inputed by user, default to 100x100'''

def Mandelbrot(rows= 100, cols = 100):
    print " **** Question 4 ****"
    print "Please wait patiently while the calculation is underway."

    
    #initialize grid and params
    threshold = 700
    upper_threshold = threshold**(2.5)
    x = np.linspace(-2,1,cols)
    y = np.linspace(-1.5, 1.5,rows)
    ''' note: we are reversing the y values so it looks like an upright grid'''
    grid = np.empty((rows,cols), dtype = np.complex128)

    grid = initialize_c_grid(x,y, grid)

    grid_2 = calculate_limit(rows, cols,upper_threshold, grid)

    mask_and_plot(grid_2, threshold)
    print "**** end of Question 4 ****"
    return 


def initialize_c_grid(x,y, grid):
    #load initial c values in to grid   
    for col_index, x_i in enumerate(x):
        for row_index, y_i in enumerate(y):
            c = x_i + 1j*y_i
            grid[row_index, col_index]  = c
    return grid

def calculate_limit(rows, cols, upper_threshold, grid):
    # initialize parameters
    N_max = 150

    # iterate through every point in the grid
    for iterator in itertools.product(range(rows), range(cols)):
        #set up 
        c = grid[iterator]
        z = c

        #iterate and calculate z N_max times
        for v in range(N_max):
            if np.abs(z) < upper_threshold:
                z = (z)**2 + c
                max_z = np.abs(z)
            
            else:  # if above upper_threshold our function will definitely determine that z diverges at point. save calculation by breaking.
                break
        grid[iterator] = z
    return grid

def mask_and_plot(grid_2, threshold):
    mask =  np.abs(grid_2)<threshold
    plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')


