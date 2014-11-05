__author__ = 'chianti'
import numpy as np

def question3():

    #First, generate a 10 x 3 array of random numbers in the range [0, 1]
    a = np.random.random_sample((10,3))

    print a

    i = range(10)
    j = np.abs(a-.5).argmin(axis=1)
    #j is the column index of the value which is closest to .5 for each row

    print 'For each row, the numbers closest to 0.5 are: \n', a[i, j]

    #Next, use abs and argsort to find the column for each of the numbers closest to .5
    print 'The column for each of the numbers closest to .5 is: '
    print np.abs(a-.5).argsort(axis=1)[:,0]

    print 'Use fancy indexing to extract the numbers into an array: '
    print a[i, j]



