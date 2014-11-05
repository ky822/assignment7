import numpy as np

def run_program():
    print '-------- Begin Question 2 --------\n'
    # Creation of array
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    print 'Array a is:\n{0}\nArray b is:\n{1}\n'.format(a, b)
    
    # Divide each column of a by b by construct an array by repeating b ncol times
    c = a / np.tile(np.reshape(b, (len(b),1)), a.shape[1])
    print 'Divide each column of a by b elementwise, the result is:\n{}\n'.format(c)

if __name__ == '__main__':
    run_program()
