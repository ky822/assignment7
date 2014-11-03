import numpy as np

# question 4(a)

def get_answer():
    print '\n----------------question 4----------------'
    # construct a grid of c= x + 1j*y values in range [-2,1]*[-1.5,1.5]
    nx, ny = 500, 500
    x = np.linspace(-2, 1 , nx)
    y = np.linspace(-1.5,1.5, ny)
    xv, yv = np.meshgrid(x, y)
    
    
    # question 4(b) do the Mandelbrot iteration
    N_max = 50
    some_threshold = 50
    c = xv + 1j*yv
    
    z = c
    for v in range(N_max):
        z = z**2 + c
        
    # question 4(c) 
    
    # form the 2-D boolean mask
    mask = abs(z) < some_threshold
    
    #save the result to an image 
    import matplotlib.pyplot as plt
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    get_answer()
    