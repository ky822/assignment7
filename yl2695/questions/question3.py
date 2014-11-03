import numpy as np


def question3():
    '''
    Generate a 10 x 3 array of random numbers in the range [0, 1] and select the closest number to 0.5 in each row.
    '''
    print 'This is question3:'
    print

    # Generate a 10 x 3 array of random numbers in the range [0, 1].
    origin_array = np.random.rand(10, 3)
    print 'The original array is: '
    print origin_array
    print

    # columnClosest is the column index of the number that is closest to 0.5
    columnClosest = np.abs(origin_array - 0.5).argsort()[:,0]
    finalArray = origin_array[np.arange(10), columnClosest]
    print 'The final array which contains the numbers that are closest to 0.5 is:'
    print finalArray
    print


if __name__ == '__main__':
    question3()