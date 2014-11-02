import numpy as np
print "\nQuestion 2 results:"
a=np.arange(25).reshape(5,5)
b=np.array([1.,5,10,15,20])
c=np.divide(a,b)#divides each column elementwise with the array c
print c 
