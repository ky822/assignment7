import numpy as np


def Question():
	#Randomly generate a 10*3 array in [0,1]
	ary = np.random.uniform(0, 1, size=30).reshape(10,3)

	#Argsort by the elements' absolute difference between 0.5 
	idx = np.argsort( np.abs(ary - 0.5), axis=1 )

	#Get the indices of those elements
	idx_col = np.transpose(idx[:, 0:1])
	idx_row = np.arange(10)

	print ary[idx_row, idx_col]


