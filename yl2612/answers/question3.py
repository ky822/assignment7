import numpy as np
def runAnswers():
    print '-----------------Question 3-----------------'
    #create a random array
    array = np.random.rand(10,3)
    print 'The random array is:\n{}\n'.format(array)
    
    #Qa and Qb: Find the column for each of the numbers closest to 0.5 on each row
    find_nearest_column_index = np.abs(array-0.5).argsort()[:, 0]
    
    #Qc: Extract the numbers into an array
    add_row_index = np.arange(len(array))
    nearest_numbers_array = array[add_row_index, find_nearest_column_index]
    print 'The new array containing the number closest to 0.5 in each row is:\n{}\n'.format(nearest_numbers_array)
    
if __name__ == '__main__':
    runAnswers()