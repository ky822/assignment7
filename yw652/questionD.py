import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis


def compMandelBrot(N_max, threshold, nx, ny):
    x = np.linspace(-2,1,nx)
    y = np.linspace(-1.5,1.5,ny)
    #c-value
    c = x[:, newaxis] + 1j * y[newaxis, :]

    #Mandelbrot iteration

    z = c
    for v in range(N_max):
        z = z**2 + c

    mandelbrotSet = (abs(z) < threshold)
    return mandelbrotSet

def questionD():
    mandelbrotSet = compMandelBrot(50, 50, 500, 500)

    #plotting the graph
    plt.imshow(mandelbrotSet.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('Mandelbrot.png')