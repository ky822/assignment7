import numpy as np

def get_answer():
    print '\n----------------question 1----------------\n'
    # create the initial array
    initial_array = np.arange(1,16).reshape(3,5)
    result_array = initial_array.transpose(1,0)
    print '\nThe intial array is:'
    print result_array
    
    # question 1(a)
    array_a = result_array[[1,3], :]
    print '\nThe array contains the 2nd and 4th rows:'
    print array_a
    
    # question 1(b)
    array_b = result_array[:,1]
    print '\nThe array contains the 2nd column:'
    print array_b
    
    #question 1(c)
    array_c = result_array[[1,2,3],:]
    print '\nThe array contains all the elements in the rectangular section between the coordinates [1,0] to [3,2]:'
    print array_c
    
    #question 1(d)
    sel = np.logical_and(result_array>=3, result_array <= 11)
    print '\nThe array contains only elements whos values are between 3 and 11:'
    print result_array[sel]

if __name__ == '__main__':
    get_answer()