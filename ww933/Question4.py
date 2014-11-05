__author__ = 'chianti'

import numpy as np
import matplotlib.pyplot as plt

def Mandelbrot(n = 300):

    #Constructing a grid of c = x + 1j*y values in range [-2, 1] x [-1.5, 1.5]
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5, 1.5, n)
    grid_x, grid_y = np.meshgrid(x, y)

    #Do the iteration
    N_max = 50
    some_threshold = 50

    c = grid_x + grid_y*1j
    z = c

    for v in range(N_max):
        z = z**2 + c

    #Form a 2-D boolean mask indicating which points are in the set
    #Here, a point (x,y) belongs to the Mandelbrot set if abs(z) < some_threshold
    mask = abs(z) < some_threshold

    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

