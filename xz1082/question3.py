import numpy as np

def answers():
    print '\n------------this is question 3---------------'
    array = np.random.rand(10, 3)
    print 'The initial array is:\n{}\n'.format(array)
    
    #3a
    #find the minimum number in each row after subtracting 0.5 from each element in the matrix
    array_close_to_half = abs(array - 0.5).min(axis = 1)
    
    #3b
    #argsort the elements in each row of the new matrix after subtracting each element by 0.5
    row_sort = np.argsort(abs(array - 0.5), axis = 1)
    #select the first column in the new matrix which is the index of the number closet to 0.5 in each row
    column_index = row_sort[:, 0]
    
    #3c
    #create an array with range(0, number of rows)
    row_index = np.arange(len(array))
    #fancy indexing 
    result_array = array[row_index, column_index]
    
    print 'New array containing the values closest to 0.5 in each row of original array is:\n{}\n'.format(result_array)

if __name__ == '__main__':
    answers()
