import numpy as np


def Question_1():
    print " **** Question 1 ****"

    initial_array = np.array(range(1,16))
    matrixlike = initial_array.reshape(5,3)

    array_2_4 = np.append(matrixlike[1], matrixlike[3])

    print "Generate a new array contain the 2nd and 4th rows. ", array_2_4
    print "------------------"


    array_col_2 = matrixlike[:,1]

    print "Generate a new array that contains the 2nd column", array_col_2
    print "------------------"


    sub_square = matrixlike[1:4, 0:3]

    print "Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] to [3,2].", sub_square
    print "------------------"


    C = matrixlike.flatten()

    temp = C[C>=3]

    temp2 = temp[temp<=11]

    print "contains only elements who's values are between 3 and 11", temp2

    print "**** end of Question 1 ****"


