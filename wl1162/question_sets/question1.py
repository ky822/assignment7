import numpy as np

def question1():
    array=np.arange(1, 16).reshape(3, 5).T
    print array

    array_a=array[[1, 3]]
    print array_a

    array_b=array[:, 1]
    print array_b

    array_c=array[1:4, :]
    print array_c

    array_d_intermediate = array[array>3]
    array_d=array_d_intermediate[array_d_intermediate<11]
    print array_d