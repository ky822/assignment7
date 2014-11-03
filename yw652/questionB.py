from numpy import *
import numpy as np

def questionB():

    #Create a 5*5 matrix with numbers in range of 25 in the given form
    arrayGiven = np.arange(25).reshape(5,5)
    arrayGivenT = arrayGiven.T

    #Divide each row element wise by the following array
    divider = np.array([1., 5, 10, 15, 20])
    temp = arrayGivenT/divider

    '''
    arrayGiven/divider[:, np.newaxis]
    '''

    #change it back to the usual form
    print temp.T



