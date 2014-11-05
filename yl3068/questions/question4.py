import numpy as np
import matplotlib.pyplot as plt

def result():
    print '\nQuestion Four:\n'

    #Construct a grid
    nx,ny = (500,500)
    x = np.linspace(-2,1,nx)
    y = np.linspace(-1.5,1.5,ny)
    xv, yv = np.meshgrid(x,y)
    c = xv + 1j*yv

    #Do the iteration
    N_max = 50
    some_threshold = 50
    z = c
    for v in range(N_max):
        z = z**2 + c

    #Form a mask
    mask = abs(z) < some_threshold

    #Save the result to an image
    plt.imshow(mask.T, extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')


