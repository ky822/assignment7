import numpy as np

def Problem1():
    
    array = np.arange(1,16).reshape(3,5).T

    a = array[[1,3],:]

    b = array[:,1]

    c = array[1:4,0:3]

    mask = (2 < array) * (array < 12)
    indices = np.where(mask)
    
    d = array[indices]

    

    return array, a, b, c, d

def main():

    array, a, b, c, d = Problem1()
    print ("the original array is \n {} \n the new array containing the 2nd and 4th rows is \n {} \n a new array with only the second column is \n {} \n a new array in with coordinates [1,0] to [3,2] is \n {} \n a new array with only elements between the value 3 and 11 is \n {}".format(array, a, b, c, d))

if __name__ == "__main__":
    main()