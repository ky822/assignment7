import numpy as np

def result():

    print '\nQuestion Three:\n'

    #Generate 10*3 array of random numbers in the range [0,1].
    initial = np.random.rand(10,3)
    print 'The initial random array is:\n{}\n'.format(initial)

    #Question a: pick the number closest to 0.5 for each row
    initial_a = abs(initial-0.5).min(axis=1)

    #Question b: find the column for each of the numbers closest to 0.5
    colunm_ix = (abs(initial-0.5).argsort())[:,0]

    #Question c: a new array containing numbers closest to o.5 in each row
    row_ix = np.arange(len(initial))
    result = initial[row_ix, colunm_ix]
    print 'The result array containing numbers closest to 0.5 in each row of initial array is:\n{}\n'.format(result)





