import numpy as np

def question2():
    a = np.arange(25).reshape(5,5)
    b = np.array([1., 5, 10, 15, 20])

    result = a.T/b

    print result.T



