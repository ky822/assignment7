"""Problem 3
Write a module to generate a 10 x 3 array of random #s in range [0,1].
a. For each row, pick the # closest to 0.5
b. Use abs and argsort to find column for each of the #s closes to 0.5
c. Fancy indexing to extract #s into an array"""

import numpy as np

def problem3():
    array = np.random.rand(10,3)
    print '\n Problem 3\'s array is: \n\n', array
    absolute_difference = abs(array-0.5)
    sorted_array = np.argsort(absolute_difference, axis=1)
    new_array_3a = array[np.arange(10), sorted_array[:, 0]]
    print 'Array of number closest to 0.5 in each row is: \n', new_array_3a
    
if __name__=='__main__':
    problem3()