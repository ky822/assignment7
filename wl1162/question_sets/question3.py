import numpy as np

def question3():
    array=np.random.rand(10,3)

    difference=abs(array-0.5)  # find the differences with 0.5

    rank=np.argsort(difference)  # find the column index of the smallest elements

    result=array[np.arange(10), [rank.T[0]]]  # fancy index

    print result
