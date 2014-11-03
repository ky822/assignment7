import numpy as np

def answers():
    print '------------this is question 1---------------'
    array = np.arange(1,16).reshape(3,5)
    result_array = array.transpose(1,0)
    print 'The initial array is:\n{}\n'.format(result_array)

    #1a
    array_a = result_array[[1,3], :]
    print 'New array containing the 2nd and 4th rows is:\n{}\n'.format(array_a) 

    #1b
    array_b = result_array[:, 1]
    print 'New array containing the 2nd column is:\n{}\n'.format(array_b)

    #1c
    array_c = result_array[1:4, :]
    print 'New array containing rectangular area between [1,0] and [3,2] is:\n{}\n'.format(array_c)

    #1d
    sel = np.logical_and(result_array >= 3, result_array <= 11)
    array_d = result_array[sel]
    print 'New array containing elements between 3 and 11 is:\n{}\n'.format(array_d)
    
if __name__ == '__main__':
    answers()