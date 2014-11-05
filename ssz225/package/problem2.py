"""Problem 2
Write a module that, given the array:
    a = np.arange(25).reshape(5,5)
divides each column elementwise with the array:
    b = np.array([1., 5, 10, 15, 20])
and prints the result"""

import numpy as np

def problem2():
    #Create [5x5] array with arange(25)
    a = np.arange(25).reshape(5,5)
    #Divide each column in a elementwise with b
    b = np.array([1., 5, 10, 15, 20])
    c = a.transpose() / b
    d = c.transpose()
    print '\n Problem 2. \n\n', d

if __name__ == '__main__':
    problem2()