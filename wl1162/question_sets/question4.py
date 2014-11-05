import numpy as np
import matplotlib.pyplot as plt

def question4():
    N_max=50
    some_threshold=50

    x=np.linspace(-2,1,500)  # evenly divide range of x into 500 pieces
    y=np.linspace(-1.5,1.5,500)  # evenly divide range of y into 500 pieces

    c=x[:, np.newaxis] + 1j*y[np.newaxis, :]  # create a grid of complex plane       
    z=c

    for i in range(N_max):
        z = z*z + c
    
    mask = (abs(z) < some_threshold)

    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')    
