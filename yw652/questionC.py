import numpy as np


def questionC():
    #Create the given matrix (random number between 0 and 1)
    givenArray = np.random.uniform(0,1, size = 30).reshape(10,3)

    #Find the distance to 0.5 for each element
    distanceTohalfTemp = np.abs(givenArray - 0.5)

    #sort the index by their distance to 0.5
    distanceTohalf = np.argsort(distanceTohalfTemp, axis=1)
    rowNumber = np.arange(10)
    colNumber = distanceTohalf[:,0]

    #print the array of 10 elements that represent the one that's closest to 0.5 for each row
    print givenArray[rowNumber,colNumber]



