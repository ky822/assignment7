
import numpy as np


def question1():
    '''
    Create a 2-D array and do a series of operations on it.
    '''
    print 'This is question1:'
    print

    # Generate the original array.
    array = []
    for i in range(5):
        new = filter((lambda x: (x % 5) == (i + 1) % 5), range(1, 16))
        array.append(new)
    array = np.array(array)
    print 'This is the original array:'
    print array
    print
    
    # Generate a new array contain the 2nd and 4th rows.
    new_array_1 = np.array([array[1], array[3]])
    print 'This is the 2nd and 4th rows:'
    print new_array_1
    print
    
    # Generate a new array that contains the 2nd column.
    new_array_2 = array[:, 1]
    print 'This is the 2nd column:'
    print new_array_2
    print
    
    # Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] to [3,2].
    new_array_3 = array[1:4, 0:3]
    print 'These are all the elements in the rectangular section between the coordinates [1,0] to [3,2]:'
    print new_array_3
    print
    
    # Generate a new array that contains only elements whose values are between 3 and 11.
    new_array_4 = array[(array >= 3)][array[(array >= 3)] <= 11]
    print 'These are the elements between 3 and 11:'
    print new_array_4
    print

if __name__ == '__main__':
    question1()