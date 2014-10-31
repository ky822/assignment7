'''
Created on Oct 29, 2014

In <demo.py>:
    Class definition of the base class Demo, which includes the declaration of pre-load arrays for each question and some basic operations that are shared by all the questions

@author: luchristopher
'''

import numpy as np
import matplotlib.pyplot as plt

class Demo():
    '''
    In class Demo:
    >>>
    Attributes:
        _the_array : The pre-loaded arrays
    Methods:
        _displayArrayDemo() : print the pre-loaded(original) array '_the_array'
        demoShow() : print the solutions of each question
    '''


    def __init__(self):
        '''
        Costructor : declaration of the pre-load array 
        '''
        self._the_array = None
        
        
    def _displayArrayDemo(self):    #protected
        print self._the_array
        
    def demoShow(self): #public
        pass