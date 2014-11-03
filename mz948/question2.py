import numpy as np



def get_answer():
    print '\n----------------question 2----------------\n'
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    
    # transpose b 
    b_transpose = b[:, np.newaxis]
    result = np.divide(a,b_transpose)
    print result
    
if __name__ == '__main__':
    get_answer()