'''
Created on Oct 30, 2014

@author: ds-ga-1007
'''
import numpy as np

def main():
    print '-----Question3-----'
    #create a 10*3 array of random numbers in the range [0,1].
    array = np.random.rand(10,3)
    print 'The 10*3 array of random numbers in the range [0,1] is:'
    print array

    #Use abs and argsort to find the column for each of the numbers closest to 0.5.
    closest_column_index = np.abs(array-0.5).argsort()[:,0]
    #use fancy indexing to extract the numbers into an array
    array_result = array[np.arange(10),closest_column_index]
    print 'The array that contains the number closest to 0.5 from the corresponding row is:'
    print array_result
    
    print '----------------'
if __name__ == '__main__':
    main()