import numpy as np
import matplotlib.pyplot as plt


def Mandelbrot(N_max, threshold, x, y):

	#Generate the points within the area	
	c =  np.expand_dims(x, axis=1) + np.expand_dims(1j * y, axis=0)

	#Iteration
	z = c
	for v in range(N_max):
		z = z**2 + c

	#Return the boolean mask
	return np.abs(z) < threshold


def Question():

	#Mandelbro iteration
	MandelbrotSetMask = Mandelbrot(50, 50, np.linspace(-2, 1, 301), np.linspace(-1.5, 1.5, 301))

	#Plot
	plt.imshow(MandelbrotSetMask.T, extent=[-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig("mandelbrot.png")


