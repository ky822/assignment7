'''

@author: jiminzi
'''
from numpy import *
def question1():
    # create the array 
    array_a=range(1,16)
    array_a=array(array_a)
    array_a=array_a.reshape((3,5))
    array_a=transpose(array_a)
    #array_a=array([[1+m+n*5 for n in range(3)] for m in range(5)])
    print'the 2d-array'
    print array_a 
    
    def question1a():
        # pick the 2econd and 4th rows
        array_1=array_a[[1,3],:]
        print
        print '2ed and 4th rows'
        print array_1
    def question1b():
        # choose the 2ed colunm of array
        array_2=array_a[:,1]
        print
        print 'Generate a new array that contains the 2nd column'
        print array_2
    def question1c():
        # choose the rectangel section
        array_3=array_a[1:4,0:3]
        print
        print ' new array that contains all the elements in the rectangular section between the coordinates[1,0] to [3,2]'      
        print array_3
    def question1d():
        # pick from 3 to 11
        array_4=array_a[logical_and(array_a<=11,array_a>=3)]
        print
        print 'elements between 3 and 11'
        print array_4
   # print all arrays
    print 'question1:\n'
    question1a()
    question1b()
    question1c()
    question1d()
if __name__ == '__main__':
    question1()