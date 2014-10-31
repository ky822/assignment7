'''
Created on Oct 29, 2014

@author: luchristopher
'''

import numpy as np
from userexcps import *

class NumericalIterator():
    '''
    In class NumericalIterator1D:
    >>>
    Attributes:
        __iter_array : The array containing the result of the iteration
        __max_iterations: The maximum number of iterations
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    


class MandelbrotIterator(NumericalIterator):
    '''
    In class MandelbrotIterator:
    '''
    
    def __init__(self, params, steps, N_max):
        '''
            construct a complex grid for mandelbrot iteration, params = [x_start,x_end,y_start,y_end], steps = [x_steps,y_steps]
        '''
        if type(params) != list or type(steps) != list:
            raise ParameterTypeError('unexpected parameter type')
        if len(params) != 4 or len(steps) != 2:
            raise ParameterFormatError('unexpected input arguments')
        #if no exceptions are raised use parameters to create the iteration array
        self.__max_iterations = N_max
        x_array = np.linspace(params[0], params[1], steps[0])
        y_array = np.linspace(params[2], params[3], steps[1])
        x, y = np.meshgrid(x_array, y_array)   
        self._iter_array = x + 1j*y #add x and y matrix elementwisely to obtain the complex matrix
        self.__c = self._iter_array
        
    def __compute(self):
        for v in range(self.__max_iterations):
            self._iter_array = self._iter_array**2 + self.__c
            
    def getValue(self):
        self.__compute()
        return self._iter_array
    
    
        
        
        
        
        
        
        