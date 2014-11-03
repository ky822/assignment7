import numpy as np
def runAnswers():
    print '-----------------Question 2-----------------'
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    #Add an axis to an array
    c = b[:, np.newaxis]
    array = np.divide(a,c)
    print 'The array I get by dividing each column of a elementwise with b is:\n{}\n'.format(array)
    
    
if __name__ == '__main__':
    runAnswers()
