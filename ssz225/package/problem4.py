"""Write a module that computes the Mandelbrot fractal using
the Mandelbrot iteration:
N_max = 50
some_threshold = 50
c = x + 1j*y
z = c
for v in range(N_max):
    z = z**2 + c
A point (x,y) belongs to the Mandelbrot set if
abs(z) < some_threshold"""
import numpy as np
import matplotlib.pyplot as plt

def problem4():
    #4a. Construct grid of c = x + 1j*y values in 
    #range [-2,1] x [-1.5, 1.5]
    #Create mesh grid with 1000 points between start:end inclusive for x,y axes
    gridx = np.linspace(-2, 1, 1000)
    gridy = np.linspace(-1.5, 1.5, 1000)
    x, y = np.meshgrid(gridx,gridy)
     
    #4b. Do the iteration
    c = x + 1j*y
    z = c
    N_max = 50
    some_threshold = 50
    
    for v in range(N_max):
        z = z**2 + c
     
    #4c. Form a 2-D boolean mask indicating which points are in the set
    #point (x,y) is in set if abs(z) < some_threshold
    mask = abs(z) < some_threshold
     
    plt.imshow(mask.T, extent = [-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    problem4()