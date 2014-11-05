'''
Created on Oct 30, 2014

@author: ds-ga-1007
'''
import numpy as np

def main():
    print '-----Question1-----'
    #create the 2-D array.
    array = np.array(np.arange(1,16)).reshape(3,5).T
    print 'The initial 2-D array is:'
    print array
    
    #Question1 a.
    #generate a new array that contains the 2nd row and 4th row.
    array_2and4_row = array[[1,3]]
    print 'The 2nd and 4th row of array is:'
    print array_2and4_row
    
    #Question1 b.
    #generate a new array that contains the 2nd column.
    array_2nd_col = array[:,1]
    print 'The 2nd column of array is:', array_2nd_col
    
    #Question1 c.
    #generate a new array that contains all the elements in the rectangular section between
    #the coordinates [1,0] to [3,2].
    array_rectangular = array[1:4,:]
    print 'The new array that contains all the elements between the coordinates [1,0] to [3,2]  is:'
    print array_rectangular
    
    #Question1 d.
    #generate a new array that contains elements between 3 and 11.   
    array_value_3to11 = np.sort(array[np.logical_and(array >= 3,array <= 11)])
    print 'The new array that contains only elements between 3 and 11 is:'
    print array_value_3to11
    
    print '----------------'
if __name__ == '__main__':
    main()