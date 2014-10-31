import numpy as np

def problem2():
    a = np.arange(25).reshape(5,5)
    b = np.array([1., 5, 10, 15, 20])
    test = a.transpose()/b
    print test.transpose()
