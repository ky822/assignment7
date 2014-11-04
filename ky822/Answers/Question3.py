'''
Created on Nov 3, 2014

@author: ds-ga-1007
'''
import numpy as np

def Question3():
    """Write a module to generate a 10*3 array of random numbers in the range [0,1]."""
    print '------Question 3------'
    
    #Generate a 10*3 array of random numbers in the range [0,1].
    random_numbers_array = np.random.rand(10,3)
    print 'The 10*3 array of random numbers in the range [0,1] is: '
    print random_numbers_array 
    print ''
    
    # The closest_index is the column index of the number that is closest to 0.5.
    for row in random_numbers_array:
        temp_array = abs(random_numbers_array - np.array([0.5,0.5,0.5]))
        array_index = np.argsort(temp_array,axis = 1)
        closest_index = array_index[:,0]
    
    # The closestNum is the number closest to 0.5 for each row.
    for i in range(10):
        closestNum = random_numbers_array[i,int(closest_index[i])]
        print 'The number closest to 0.5 in row '+ str(i) + ' is ' + str(closestNum) + ' in column ' + str(closest_index[i]) + '.' 
    
    # Print out a 1-D array containing 10 values of the numbers closest to 0.5
    row_index = np.arange(10)
    closestNum_array = random_numbers_array[row_index , closest_index]
    print ''
    print 'The numbers closest to 0.5 form an array: ' 
    print closestNum_array
    
    print '----------------------'
    
if __name__ == '__main__':
    Question3()