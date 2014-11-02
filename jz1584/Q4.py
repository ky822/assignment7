import numpy as np
import matplotlib.pyplot as plt
#np.set_printoptions(threshold=np.nan) #optional: to be able check the print out of whole array

N_max=50#set number of iteration be 50
some_thresdhold=50 #set the threshold for Mandelbrot be 50

#generates evenly spaced samples for x and y over each interval (by default, 50 each)
x_samples=np.linspace(-2,1)
y_samples=np.linspace(-1.5,1.5)

#constructs a grid of c = x+1j*y values based on the range of x and y 
x,y=np.meshgrid(x_samples,y_samples)
c=x+1j*y
z=c
#c.shape

for v in range(50):#do the iteration on z
    """RuntimeWarning may be expected due to extreme large element values in the iteration,
but it's not important in this case since we only care about the element less than thresdhold
    """
    z=z**2+c 

# from a 2-d boolean mask indicating which points are in the set
mask=(np.abs(z)<some_thresdhold)


#save the result to an image using mtaplotlib
# Note: since I use np.meshgrid, I dont need to find the transpose of mask
plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')
plt.show()

