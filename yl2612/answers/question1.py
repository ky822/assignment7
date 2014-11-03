import numpy as np
def runAnswers():
    print '-----------------Question 1-----------------'
    #Creates a 2-D array
    array = np.arange(1,16).reshape((3,5)).transpose()
    print 'The 2-D array is:\n{}\n'.format(array)
    
    #Qa: New array containing the 2nd and 4th row
    array_row_2_and_4 = array[[1, 3]]
    print 'The new array containing the 2nd and 4th row is:\n{}\n'.format(array_row_2_and_4)
    
    #Qb: New array containing the 2nd column
    array_col_2 = array[:, 1] # what if I try array2 = array[:,1:2]?
    print 'The new array containing the 2nd column is:\n{}\n'.format(array_col_2)
    
    #Qc: New array that contains all the elements between the coordinates [1,0] to [3,2]
    array_coordinate_10_to_32 = array[1:4, :3]
    print 'The new array that contains all the elements between the coordinates [1,0] to [3,2] is:\n{}\n'.format(array_coordinate_10_to_32)
    
    #Qd: New array that contains only elements having value between 3 and 11
    array_elements_3_to_11 = array[np.logical_and(array>=3, array<=11)]
    print 'The new array that contains only elements having value between 3 and 11 is:\n{}\n'.format(array_elements_3_to_11)

    
if __name__ == '__main__':
    runAnswers()
