import numpy as np

Q1_array=np.ones((5,3))#initialize a 5 by 3 ones array
for i in range(0,5):
    "assigning new value to the array"
    Q1_array[i]=np.arange(i+1,12+i,5)
   
print "\n Q1 Array: \n", Q1_array

#a
indices=np.array([1,3])
a_array=Q1_array[indices]#Generate a new array contain the 2nd and 4th rows
print "\n Array a: \n", a_array
#b
b_array=Q1_array[:,1]#Generate a new array that contains the 2nd column
print "\n Array b: \n",b_array
#c
c_array=Q1_array[1:4,:]#Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] to [3,2].
print "\n Array c: \n",c_array
#d
d_array=Q1_array[np.logical_and(Q1_array >3, Q1_array < 11)]
#Generate a new array that contains only elements who's value btw 3 and 11
print "\n Array d: \n",d_array


