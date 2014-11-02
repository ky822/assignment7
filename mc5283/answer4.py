import numpy as np
import matplotlib.pyplot as plt

def run():
    print '----------------Question 4-----------------'
    x,y=np.ogrid[-2:1:5000j,-1.5:1.5:5000j]
    c=x + 1j*y
    z=0

    N_max = 50
    for g in range(N_max):
        print('Iteration number: ',g)
        z=z**2 + c
        
    threshold = 50
    mask=np.abs(z) < threshold
    
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    run()
