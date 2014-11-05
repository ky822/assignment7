import matplotlib.pyplot as plt
import numpy as np
from numpy import *

def question4():
    '''
    Compute the Mandelbrot fractal using the Mandelbrot iteration and draw a picture.
    '''
    print 'This is question4:'
    print
    # construction the grid first
    number_of_x = 500
    number_of_y = 500
    x = np.linspace(-2, 1, number_of_x)
    y = np.linspace(-1.5, 1.5, number_of_y)
    c = x[:, newaxis] + 1j * y[newaxis, :]

    # do the iteration
    N_max = 50
    some_threshold = 50
    z = c
    for v in range(N_max):
        z = z ** 2 + c
    mask = (abs(z) < some_threshold)

    # save the result to an image
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    question4()
