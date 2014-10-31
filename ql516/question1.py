import numpy as np

def array_create():
    """
    create the required array in the question 1
    """
    #first: creat a array from 1 to 15 
    array = np.arange(1,16)
    #reshape it into a 3 * 5 matrix
    array = array.reshape((3,5))
    #transpose it 
    array = array.T
    print "The array is:\n",array
    return array

def question_a(array):
    """
    a: print  the 2nd and 4th rows of the array
    """
    array_slice = array[(1,3),:]
    print "its 2nd and 4th rows is:\n",array_slice

def question_b(array):
    """
    b: print the 2nd column of the array
    """
    print "the 2nd column of the array is:\n",array[:,1]

def question_c(array):
    """
    c: generate a new array that contains all the elements
    in the rectangular section between the coordinates [1,0] to [3,2]
    """
    print "the element in the rectangular section is:\n",array[1:4,0:3]

def question_d(array):
    """
    d: generate a new array that contains only elements who's values are
    between 3 and 11
    """
    #revalled_array = array.T.ravel()
    #filtered = filter((lambda x: 3<x<11),revalled_array)
    #print "the filtered array is:\n", filtered
    
    
    filter_index = (array>2) & (array<12)
    print "the filtered array is:\n", array[filter_index]
    
def main():
    array = array_create()
    question_a(array)
    question_b(array)
    question_c(array)
    question_d(array)
    
if __name__ == "__main__":
    main()
    
    


