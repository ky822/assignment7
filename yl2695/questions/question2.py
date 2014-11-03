import numpy as np


def question2():
    '''
    create two arrays: a and b. And divide each column elementwise with b then print the result.
    '''
    print 'This is question 2:'
    print

    # initialize array a and b.
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])

    # Divide each column elementwise with the array b.
    divideResult = a / b.reshape(5, 1)

    print 'The result of a / b is:'
    print divideResult
    print

if __name__ == '__main__':
    question2()