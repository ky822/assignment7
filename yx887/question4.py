import numpy as np
import matplotlib.pyplot as plt

def run_program():

    print '-------- Begin Question 4 --------'

    # Creat a grid of x, y
    print 'Creating meshgrid ...'
    nx, ny = 300, 300
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    xv, yv = np.meshgrid(x, y)
    c = xv + 1j * yv
    
    # Do the iteration
    print 'Doing Mandelbrot iteration ...'
    N_max = 50
    threshold = 50
    z = c
    for v in range(N_max):
        z = z**2 + c

    # Get the 2-d mask
    mask = abs(z) < threshold
    
    # save the result to an image
    print 'Drawing fancy pictures ...'
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    run_program()
