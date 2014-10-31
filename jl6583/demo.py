'''
Created on Oct 29, 2014

@author: luchristopher
'''

import numpy as np
import matplotlib.pyplot as plt

class Demo():
    '''
    This is the base class
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._the_array = None
        
        
    def _displayArrayDemo(self):    #protected
        print self._the_array
        
    def demoShow(self): #public
        pass