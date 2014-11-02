import numpy as np

print "\nQuestion 3 result : \n\n A 10 x 3 array of random numbers in the range [0, 1]:"
a=np.random.rand(10,3)
print a
rowIndex=np.arange(10)#generate the index of row
Difference=np.abs(a-0.5)#find the absolute difference for each element
Index_array=np.argsort(Difference,axis =1)#find the indices that would sort the array
columnIndex=Index_array.argmin(axis=1)#find the column index of the min element in each row

OneD_array=a[rowIndex,columnIndex]
"""generates one D array that contains the number closest to 0.5 from 
the corresponding row of the original array
"""
print'\n One D array that contains the number closest to 0.5 from the corresponding row of the original array'
print  OneD_array
