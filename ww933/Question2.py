__author__ = 'chianti'

def question2():
    import numpy as np

    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])

    print 'Given the array: \n', a
    print 'divides each column elementwise with the array: \n', b

    c = a.view('float')

    for column_number in range(0, 5):
        c[:, column_number] = a[:, column_number]/b

    print 'The result is: \n', c


