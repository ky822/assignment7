import numpy as np

def answers():
    print '\n------------this is question 2---------------'
    #given arrays a and b
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    #create a new array which is array b's transpose
    b_trans = b[:, np.newaxis]
    
    #divide each column elementwise with array b_trans
    result = np.divide(a, b_trans)
    print 'Divide each column of a by b elementwise, the result is:\n{}\n'.format(result)

if __name__ == '__main__':
    answers()