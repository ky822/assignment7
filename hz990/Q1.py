import numpy as np

def Run():
	'''Answers to question 1

	'''
	print '\n--------------------Answer to question 1 ----------------------'
	# Generating the original array
	a = np.arange(1,16).reshape(3, 5).T
	print 'The original array is :\n{}\n'.format(a)

	# Part A
	ans_a = a[1:4:2]
	print 'The new array contains the 2nd and 4th rows is:\n{}\n'.format(ans_a)

	# Part B
	ans_b = a[:,1]
	print 'The new array contains the 2nd column is:\n{}\n'.format(ans_b)

	# Part C
	ans_c = a[1:4,:]
	print 'The new array contains the rectangular section is:\n{}\n'.format(ans_c)

	# Part D
	sel = (a > 2) * (a < 12)
	ans_d = a[sel]
	print 'The new array contains values between 3 and 11 is:\n{}\n'.format(ans_d)




