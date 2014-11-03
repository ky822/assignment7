import numpy as np

def Run():
	'''This function returns a 1-D array which contains the closest values to 0.5 from the original array 

	'''
	print '\n--------------------Answer to question 3 ----------------------'

	# Generating the original 10 x 3 array
	original_array = np.random.rand(10, 3)

	# Calculating the distance
	dist = abs(original_array - 0.5)

	# Sorting the distance
	index = np.argsort(dist)

	# Row and column indexing
	column_index = index[:, 0]
	row_index = np.arange(len(index))

	# Final result
	new_array = original_array[row_index, column_index]
	print 'The 1-D array  which contains the closest distance to 0.5 is :\n{}\n'.format(new_array)
