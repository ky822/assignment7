import numpy as np

def run_program():
    print '-------- Begin Question 1 --------\n'
    # Creation of array
    array = np.array(range(1, 16)).reshape((5, 3), order='F')
    print 'The initial array is:\n{}\n'.format(array)

    # Question 1.a: New array_a contain the 2nd and 4th rows
    array_a = array[[1,3]]
    print 'New array containing the 2nd and 4th rows is:\n{}\n'.format(array_a)

    # Question 1.b: New array_b contain the 2nd column
    array_b = array[:, 1]
    print 'New array containing the 2nd column is:\n{}\n'.format(array_b)

    # Question 1.c: 
    array_c = array[1:4, 0:3]
    print 'New array containing rectangular area between [1,0] and [3,2] is:\n{}\n'.format(array_c)

    # Question 1.d:
    array_d = array[(array <= 11) & (array >= 3)]
    print 'New array containing elements between 3 and 11 is:\n{}\n'.format(array_d)

if __name__ == '__main__':
    run_program()
