import numpy as np
import matplotlib.pyplot as plt

def Problem4():
    
    N_Max = 10
    some_threshold = 10

    x,y = np.ogrid[-2:1:50j,-1.5:1.5:50j]
    c = x + 1j*y
    
    z = 0
    
    for v in range(N_Max):
        z = z**2 + c
        mask = np.abs(z) < some_threshold
    
    # mask = np.abs(z) < some_threshold

    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.show()
    plt.savefig('mandelbrot.png')

    return None

def main():

    Problem4()

if __name__ == "__main__":
    main()