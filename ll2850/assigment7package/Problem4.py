__author__ = 'leilu'

import matplotlib.pyplot as plt
import numpy as np


def Mandelbrot():

    N_max = 50
    some_threshold = 50

    x, y = np.ogrid[-2:1:5000j, -1.5:1.5:5000j]

    c = x + 1j*y
    z = 0

    for v in range(N_max):
        z = z**2 + c

    m = np.abs(z) < some_threshold

    plt.imshow(m.T, extent = [-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

