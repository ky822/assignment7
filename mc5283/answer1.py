import numpy as np

def run():
    print '---------------Question 1-----------------'
    #create array
    array = np.arange(1,16).reshape(3,5).T
    print 'The initial array is:\n{}\n'.format(array)

    #Q1.a new array containing row 2 and 4
    array_2_4 = np.concatenate((array[1],array[3]), axis = 0).reshape(2,3)
    print 'The new array containing row 2 and 4 is:\n{}\n'.format(array_2_4)

    #Q1.b new arrau containing column 2
    array_2_col = array[:,1]
    print 'The new array containing column 2 is:\n{}\n'.format(array_2_col)

    #Q1.c
    start = [1,0]
    end = [3,2]
    newArray = array[start[0]:end[0]+1, start[1]:end[1]+1] 
    print 'The new array containing area between [1,0] and [3,2] is:\n{}\n'.format(newArray)

    #Q1.d
    array_3_11 = array[(array <= 11)&(array >= 3)]
    print 'The new array containing elements between 3 and 11 is:\n{}\n'.format(array_3_11)


if __name__ == '__main__':
    run()
