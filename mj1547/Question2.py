'''


@author: jiminzi
'''
from numpy import *
def Question2():
    # create the array from 0 to 24 and 5*5
    a = arange(25).reshape(5,5)
    b = array([1., 5, 10, 15, 20])
    #re shape the b array to a column
    b = b.reshape(5,1)
    #divide each column by b.reshape
    result2 = divide(a,b)
    print 'question 2\n'
    print 'divide each column of a by b by construct an array by repeating'
    print result2
 


if __name__ == '__main__':
    Question2()