import numpy as np
import matplotlib.pyplot as plt
def runAnswers():
    #Construct a grid
    x = np.linspace(-2, 1, 500)
    y = np.linspace(-1.5, 1.5, 500)
    c = x[:,np.newaxis] + 1j * y[np.newaxis,:]
    
    #Do the iteration
    N_max = 50
    some_threshold = 50
    z=c
    for v in range(N_max):
        z = z**2 + c
    
    #Form a 2-D boolean mask indicating which points are in the set
    mask = abs(z) < some_threshold
    
    #Save the Result to an image
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
        
    
if __name__ == '__main__':
    runAnswers()