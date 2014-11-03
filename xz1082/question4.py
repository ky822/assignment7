import numpy as np
import matplotlib.pyplot as plt

def answers():
    print '\n------------this is question 4---------------'
    #construct a grid in range 
    nx, ny = (500, 500) 
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    
    xv, yv = np.meshgrid(x, y)
    c = xv + 1j * yv
    
    #do the iteration
    N_max = 50
    some_threshold = 50
    
    z = c
    for v in range(N_max):
        z = z ** 2 + c
    
    #form a boolean mask indicating which points belongs to the Mandelbrot set
    mask = abs(z) < some_threshold
    
    #plot and save the image
    plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    answers()
