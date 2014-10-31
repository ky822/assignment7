import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def problem4():
    N_max = 50
    some_threshold= 50.
    x = np.linspace(-2,1,500)
    y = np.linspace(-1.5,1.5,500)
    c = x[:,newaxis] + 1j * y[newaxis,:]
    z = c

    for j in range(N_max):
        z = z**2 + c

    answer = (abs(z) < some_threshold)

    plt.imshow(answer.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig("mandelbrot.png")

