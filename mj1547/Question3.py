'''


@author: jiminzi
'''
import math
from numpy import *
def Question3():
    print'question 3'
    '''
    generate a array which from 0 to 1 and 10*3 matrices
    '''
    array_q3=random.rand(10,3)#uniform random numbers in [0,1]
    '''
    way one use for loop
    '''
    closetohalf_row=[]
    for x in range(10):
        half=find_closest(array_q3[x,:],0.5)
        x=x+1
        closetohalf_row.append(half)
    #closetohalf=find_closest_row(array_q3, 0.5)
    closetohalf_row=array(closetohalf_row)
    '''
    way 2 which I use argmin
    !!!!!!!!!!
    '''
    x=argmin(abs(array_q3-0.5),axis=1).choose(array_q3.T)
    #use fancy index of column and row
    '''
    way 3 with argsort and fancy index
    '''
    column_index=argsort(abs(array_q3-0.5))[:,0].flatten()
    row_index=arange(len(array_q3))
    new_array=array_q3[row_index,column_index]
    print '10*3 random array form 0 to 1'
    print array_q3
    print
    print 'close to 0.5 array'
    print closetohalf_row
    print 'another way'
    print x
    print 'use argsort and fancy index'
    print new_array
    
def find_closest(array,value): 
    idx = abs(array-value).argmin()
    return array.flat[idx]
if __name__ == '__main__':
    Question3()