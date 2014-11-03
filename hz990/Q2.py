import numpy as np

def Run():
	'''This function returns the column elementwise divided new array

	'''
	print '\n--------------------Answer to question 2 ----------------------'

	a = np.arange(25).reshape(5, 5)
	b = np.array([1., 5, 10, 15, 20])
	new_array = np.divide(a.T, b).T
	print 'The elementwise divided new array is :\n{}\n'.format(new_array)

