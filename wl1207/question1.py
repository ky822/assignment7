import numpy as np

def function():
	print "This is the answer to question1 is:\n"
	
	array = np.array(range(1,16)).reshape(3,5).transpose()
	print "The 2-D array is:\n",array,"\n"
    
	array_a = array[[1,3]]
	print "The new array contains the 2nd column and 4th rows is:\n", array_a, "\n"

	array_b = array[:, 1]
	print "The new array contains the 2nd column is:\n",array_b, "\n"
    
	array_c = array[1:4, :]
	print "The new array contains all the elements in the rectangular section is:\n", array_c, "\n"
    
	array_d = array[np.logical_and(array>=3, array<=11)]
	print "The new array contains all the elements between 3 and 11 is:\n", array_d, "\n"

if __name__ =='__main__':
	function()
