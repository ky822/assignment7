'''
Created on Nov 3, 2014

@author: ds-ga-1007
'''
import numpy as np

def Question1():
    """ Create a 2-D array and generate 4 new arrays."""
    print '------Question 1------'
    
    #Create the 2-D array.
    current_array = np.arange(1,16)
    target_array = current_array.reshape(5,3)
    print 'Create the 2-D array: \n', target_array
   
    # a. Generate a new array contain the 2nd and 4th rows.
    array_a = np.array([target_array[1],target_array[3]])
    print 'a. Generate a new array contain the 2nd and 4th rows: \n', array_a
    
    # b. Generate a new array that contains the 2nd column.
    array_b = target_array[:,1]
    print 'b. Generate a new array that contains the 2nd column: \n', array_b
    
    # c. Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] to [3,2].
    array_c = target_array[1:4,:]
    print 'c. Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] to [3,2]: \n', array_c
    
    # d. Generate a new array that contains only elements who's values are between 3 and 11.
    array_d = target_array[np.logical_and(target_array>=3,target_array<=11)]
    print  array_d
    
    print '----------------------'
    
if __name__ == '__main__':
    Question1()