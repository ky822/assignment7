import numpy as np



def get_answer():
    print '\n----------------question 3----------------\n'
    # create the initial array
    initial_array = np.random.rand(10,3)
    print '\nThe initial array is:'
    print initial_array
    
    # question 3(a)
    array_close_to_half = abs(initial_array - 0.5).min(axis=1)   
    
    # question 3(b)
    
    assorted_column_index = abs(initial_array - 0.5).argsort(axis = 1)
    # select the first column that contains all the indexes of the minimum absolute value of initial_array - 0.5
    closest_column_index = assorted_column_index[:,0]
    

    # question 3(c)
    closest_raw_index = np.arange(len(initial_array))
    #using the fancy indexing to get the original multi-dimensional array 
    closest_array = initial_array[closest_raw_index, closest_column_index]
    print '\nThis is the 1-D array containing 10 values, each value is the number closest to 0.5 from the corresponding row of the original array:'
    print closest_array

if __name__ == '__main__':
    get_answer()