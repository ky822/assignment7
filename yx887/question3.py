import numpy as np

def run_program():
    print '-------- Begin Question 3 --------\n'
    # Creation of random array
    array = np.random.random((10, 3))
    print 'The initial array is:\n{}\n'.format(array)

    # Question 3.a
    array_close_half = abs(array - 0.5).min(axis=1)

    # Question 3.b
    array_column_index = abs(array - 0.5).argsort()[:, 0].flatten()

    # Question 3.c
    array_row_index = np.arange(len(array))
    array_result = array[array_row_index, array_column_index]
    print 'New array containing the closest values in each row of original array is:\n{}\n'.format(array_result)

if __name__ == '__main__':
    run_program()
