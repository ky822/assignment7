import numpy as np
import matplotlib.pyplot as plt

def Run():
	'''This function returns the Mandelbrot fractal image

	'''
	# Setting initial parameters
	N_max = 50
	some_threshold = 50.
	x = np.linspace(-2, 1, 1000)
	y = np.linspace(-1.5, 1.5, 1000)

	# Constructing the grid
	c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
	z = c

	# Mandelbrot iteration
	for j in range(N_max):
		z = z**2 + c
	a = abs(z) < some_threshold

	# Printing the Mandelbrot fractal image
	plt.imshow(a.T, extent = [-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig("mandelbrot.png")

