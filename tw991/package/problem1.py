from numpy import *

def problem1():
    a = arange(1,16)
    a.resize(3,5)
    a = a.transpose()
    print a

    new2 = a[[1,3]]
    print new2

    new3 = a[:,1]
    print new3

    new4 = a[1:4, 0:3]
    print new4

    b = a[a>3]
    new5 = b[b<11]
    print new5