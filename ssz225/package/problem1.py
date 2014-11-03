import numpy as np

def problem1():
    #Problem 1
    #Generating array
    print 'Problem 1. \n'
    array = np.arange(1,16)
    array.resize(3,5)
    array = array.transpose()
    print 'Array is: \n', array
    
    #1a. Generate new array with 2nd and 4th rows
    new_array_a = array[[1,3]]
    print '1a. New array with 2nd and 4th rows is: \n', new_array_a
     
    #1b. Generate new array with 2nd column
    new_array_b = array[:,1]
    print '1b. New array with 2nd column is: \n', new_array_b
      
    #1c. Generate new array that contains all elements
    #in between [1,0] to [3,2]
    new_array_c = array[1:4,0:3]
    print '1c. New array with all elements between [1,0] and [3,2] is: \n', new_array_c
      
    #1d. Generate new array that contains only elements
    #whose values are between 3 and 11
    intermediate_new_array_d = array[array >= 3]
    new_array_d = intermediate_new_array_d[intermediate_new_array_d <= 11]
    print '1d. New array with only elements between 3 and 11 is: \n', new_array_d
    
if __name__ == '__main__':
    problem1()