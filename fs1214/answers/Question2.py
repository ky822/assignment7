'''
Created on Oct 30, 2014

@author: ds-ga-1007
'''
import numpy as np

def main():
    print '-----Question2-----'
    #create array a and b.
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    print 'The dividend array - a is:'
    print a
    print 'The divisor array - b is:'
    print b
    
    #a divides each column elementwise with b, using broadcasting.
    result = a/b.reshape(5,1)
    print 'The answer of a dividing each column elementwise with b is:'
    print result
    
    print '----------------'
if __name__ == '__main__':
    main()