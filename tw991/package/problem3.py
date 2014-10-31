from numpy import *
import numpy as np

def problem3():
    test = np.random.rand(10,3)
    a = abs(test-0.5)
    order = np.argsort(a,1)
    order_first = order[:,0]
    small = test[arange(10),order_first]
    print small