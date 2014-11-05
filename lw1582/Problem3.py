import numpy as np

def Problem3():

    array = np.random.rand(10,3)

    order = np.argsort(abs(array-0.5), axis=1)

    a = array[np.arange(array.shape[0])[:, None],order]
    
    b = np.argmin(abs(array-0.5), axis = 1)

    c = [array[i, b[i]] for i in range(0,b.size)]

    return array, a, b, c

def main():

    array, a, b, c = Problem3()

    print ("the 10 * 3 array is \n {} \n the number closest to 0,5 for each row is in the first column \n {} \n to the column with closest value to 0.5 for each row is \n {} \n and these numbers are: \n {} \n".format(array, a, b, c))

if __name__ == "__main__":
    main()
