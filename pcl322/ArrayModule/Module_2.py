import numpy as np

def Question():
	a = np.arange(25).reshape(5, 5)
	b = np.array([1., 5, 10, 15, 20])

	#Divide each column elementwise
	print a/b[:, np.newaxis]
