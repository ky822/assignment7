import numpy
import numpy as np
from numpy import *

def questionA():
    #initialize the given array
    givenArray = np.arange(1, 16).reshape(3, 5).T

    #Retrieve the second and fourth row and put them into a 2*3 matrix
    arrayA = np.concatenate((givenArray[1], givenArray[3]), axis=0).reshape(2, 3)

    #Retrieve the second column of the given matrix
    arrayB = givenArray[:, 1]

    #Get numbers in the given position (question 1c)
    arrayC = givenArray[1:4, 0:3]

    #Get numbers from 3 to 11
    arrayDList = []
    for i in range(5):
        for j in range(3):
            if (givenArray[i][j] > 3) and (givenArray[i][j] < 11):
                arrayDList.append(givenArray[i][j])

    arrayD = np.array(arrayDList)

    print givenArray
    print arrayA
    print arrayB
    print arrayC
    print arrayD


