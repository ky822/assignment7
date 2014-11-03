import numpy as np

def result():
    print '\nQuestion One:\n'

    #Generate the initial array
    initial = np.arange(1,16,1).reshape((3,5)).transpose()
    print 'The initial array is :\n{}\n'.format(initial)

    #Question a: generate a new array that contains the 2nd and 4th rows
    initial_a = initial[(1,3), :]
    print 'A new array containing the 2nd and 4th rows is :\n{}\n'.format(initial_a)

    #Question b: generate a new array that contains the 2nd column
    initial_b = initial[:,1]
    print 'A new array containing the 2nd colunm is :\n{}\n'.format(initial_b)

    #Question c: generate a new array that contains all the elements between [1,0] and [3,2].
    initial_c = initial[1:4, :]
    print 'A new array containing elements in the rectangular section between [1,0] and [3,2] is :\n{}\n'.format(initial_c)

    #Question d: generate a new array that contains elements who's value are between 3 and 11
    selection_d = (initial >= 3) * (initial <= 11)
    initial_d = initial[selection_d]
    print 'A new array containing elements whose value are between 3 and 11 is :\n{}\n'.format(initial_d)

