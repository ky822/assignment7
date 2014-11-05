import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def function():
	print "This is the answer to question4:\n"
	
	N_max = 50
	some_threshold = 50
    
	x, y = np.ogrid[-2:1:5000j, -1.5:1.5:5000j]
    
	c = x + 1j*y
	z = 0
    
	for v in range(N_max):
		z = z**2 +c
        
	mask = np.abs(z) < some_threshold
    
	plt.imshow(mask.T, extent = [-2,1,-1.5,1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')
    
if __name__ =='__main__':
    function()
