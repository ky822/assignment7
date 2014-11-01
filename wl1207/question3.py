import numpy as np

def function():
	print "This is the answer to question3:\n"
	
	array = np.random.rand(10,3)
	index = abs(array-0.5).argmin(axis = 1)
	print "The initial array is:\n", array, "\n"
    
	array_a = array[np.arange(10),index]
	print "The number in each row closest to 0.5 is:\n", array_a, "\n"
    
	index_sort = np.argsort(abs(array-0.5), axis = 1)
	array_b = array[np.arange(10), index_sort[:,0]]
	print "The number in each row closest to 0.5 is:\n", array_b, "\n"
    
    
if __name__ =='__main__':
    function()
