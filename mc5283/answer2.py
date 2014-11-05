import numpy as np

def run():
    print '-------------Question2---------------'
    #create arrays
    a = np.arange(25).reshape(5,5).T
    b = np.array([1., 5, 10, 15, 20])
    divide = np.divide(a,b).T
    print 'divide each column of a by b lementwise, the result is:\n{}\n'.format(divide)

if __name__ == '__main__':
    run()

