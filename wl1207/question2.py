import numpy as np


def function():
    print "This is the answer to question2:\n"
	
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    divided = a.transpose()/b
    print "The array after divided is:\n", divided.transpose(), "\n"
    
if __name__=='__main__':
    function()
