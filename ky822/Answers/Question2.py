'''
Created on Nov 3, 2014

@author: ds-ga-1007
'''
import numpy as np

def Question2():
    """Create array a , and divide each column elementwise with b."""
    print '------Question 2------'
    
    #Create the  array a and b given by the  question. 
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    print 'Given the array a and b: \n', a,b
    
    # Divide each column elementwise with the array.
    result = np.zeros(25).reshape(5,5)
    for column_index in range(5):
        result[:,column_index] = a[:,column_index]/b
    print 'The result is : '
    print result
    
    print '----------------------'
    
if __name__ == '__main__':
    Question2()