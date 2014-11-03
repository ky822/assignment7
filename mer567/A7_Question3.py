import numpy as np 
from numpy.random import rand 



def Question_3():
    print " **** Question 3 ****"
    '''np.random.seed(0) # set seed for easy testing.'''
    a = rand(10,3) # generate the 2D array

    #subtract 0.5 from every element in the array and take its absolute value
    b = np.abs(a - 0.5)

    #find entries closest to 0.5
    d = np.argsort(b, axis = 1)
    col_index = d[:,0] 
    row_index = range(10)
    
    print " 1-D array each value is the number closest to 0.5 from the corresponding row of the original array."

    # use fancy indexing to find to find the closest elements in original array.
    print a[row_index,col_index]
    print "**** end of Question 3 ****"
    return
