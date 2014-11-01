import numpy as np

def divideArray ():

    a = np.arange(25).reshape(5,5)

    b = np.array([1.,5,10,15,20])

    c = a / b[np.newaxis,:]
    
    return a, b, c 
    
def main():
    
    a, b, c =divideArray()
    print "a is = " + '\n' + np.array_repr(a, precision = 2)
    print "each column divided by b = " + np.array_repr(b, precision = 2)
    print "is equal to " + '\n' + np.array_repr(c, precision = 2)

if __name__ == "__main__":
    main()