import numpy as np

def result():

    print '\nQuestion Two:\n'
    #Generate initial array a and b
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    print 'Array a is :\n{0}\n\nArray b is :\n{1}\n'.format(a, b)

    #Divides each column in a with the array b
    c = (a.T / b).T
    print 'The result dividing each colunm in a with the array b is :\n{}\n'.format(c)

