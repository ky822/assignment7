import numpy as np


def Question_2():
    print " **** Question 2 ****"
    a = np.arange(25).reshape(5, 5)

    
    b = np.array([1., 5, 10, 15, 20])

    # divide each column with b
    c = a / b[:,None]

    print "divides each column elementwise with the array"
    print  c

    print "**** end of Question 2 ****"



