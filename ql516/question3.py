# -*- coding: utf-8 -*-

import numpy as np

def array_generate():
    """
    generate a 10x3 array of random numbers in range[0,1]
    """
    array = np.random.rand(10,3)
    return array
    
def GetClosestNumber(array):
    """
    for each row, pick the number closest to .5
    """
    min_index = np.argmin(np.abs(array-0.5),1)
    closest_array = array[np.arange(10),min_index]
    return closest_array
    
def GetClosestNumberBySort(array):
    """
    Generte an array contain the numbers closest to 0.5 in each rows
    
    Argument
    ========
    array: numpy array 
    
    Return
    ======
    an array contain the closest numbers
    
    Example
    =======
    >>>array1 = array_generate()
    >>>array1
    array([[ 0.63665097,  0.50696162,  0.76121097],
       [ 0.68714886,  0.20228392,  0.52424866],
       [ 0.3275332 ,  0.76667842,  0.41314787],
       [ 0.05645787,  0.6146244 ,  0.69211519],
       [ 0.13655137,  0.84564668,  0.57381465],
       [ 0.65070546,  0.7825995 ,  0.67390848],
       [ 0.23796975,  0.97312122,  0.87593416],
       [ 0.39804522,  0.30356075,  0.79707104],
       [ 0.45504483,  0.28996881,  0.71733035],
       [ 0.94605093,  0.65489037,  0.54693193]])
    >>>print GetClosestNumberBySort(array1)
    array[ 0.50696162  0.52424866  0.41314787  0.6146244   0.57381465  0.65070546
           0.23796975  0.39804522  0.45504483  0.54693193]

    """
    row_number = 10
    array_abs = np.abs(array-0.5)
    array_sorted_index = np.argsort(array_abs)
    sorted_array = array[np.arange(row_number).reshape((row_number,1)),array_sorted_index]
    closest_array = sorted_array[:,0]
    return closest_array
    
def main():
    array = array_generate()
    print array
    #print "get closest number: \n",GetClosestNumber(array)
    print "get closest number for each row: \n", GetClosestNumberBySort(array)
    


if __name__ == "__main__":
    main()
    
    
    
    