__author__ = 'chianti'

def question1():

    import numpy as np

    #create the desired 2-D array
    array = np.array(range(1,16)).reshape((5,3), order='F')
    print array

    #a. Generate a new array contain the 2nd and 4th rows
    new_array = array[[1, 3]]
    print 'A new array that contains the 2nd and 4th rows: \n', new_array

    #b. Generate a new array that contains the 2nd column
    SecondColumn = array[:, 1]
    print 'A new array that contains the 2nd column: \n', SecondColumn

    #c. Generate a new array that contains all the elements in the rectangular section
    #   between the coordinates [1,0] to [3,2]
    RectangularArray = array[1:4, :]
    print 'a new array that contains all the elements in the rectangular section between the coordinates ' \
          '[1,0] to [3,2]: '
    NewArray = RectangularArray.ravel()
    print NewArray

    #d. Generate and a new array that contains only elements with values are between 3 and 11
    ElemetsBetweenThreeAndEleven = array[(array >= 3) & (array <= 11)]
    print 'A new array that contains only element' \
          's with values are between 3 and 11: \n', ElemetsBetweenThreeAndEleven



