import numpy as np

def run():
    print '----------------Question 3-----------------'
    #create a random array
    array = np.random.rand(10,3)
    #Q3.a
    closest = np.argmin(abs(array-0.5), axis = 1).choose(array.T)
    #Q3.b
    column = np.argsort(abs(array-0.5), axis = 1)[:,0]
    #Q3.c
    row = np.arange(len(array))
    result = array[row, column]
    print 'The number closest to 0.5 in each row:','\n',closest,'\n','The column of the smallest number:','\n',column,'\n','The new array containing the closest values is:','\n',result
if __name__ == '__main__':
    run() 
