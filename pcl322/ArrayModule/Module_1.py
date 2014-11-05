import numpy as np

def Question_a():
	#Select the 2nd and 4th rows
	ary = np.transpose(np.arange(1, 16).reshape(3, 5))
	print ary[1:4:2]

def Question_b():
	#Select the 2nd columns
	ary = np.transpose(np.arange(1, 16).reshape(3, 5))
	print np.transpose(ary[::, 1:2])

def Question_c():
	#Get the elements within rectangle between [1,0] and [3,2]
	ary = np.transpose(np.arange(1, 16).reshape(3, 5))
	print ary[1:4, 0:3]

def Question_d():
	#Get the elements whose values are bewteen 3 and 11
	ary = np.transpose(np.arange(1, 16).reshape(3, 5))
	print ary[np.logical_and(ary >= 3, ary <= 11)]
	
