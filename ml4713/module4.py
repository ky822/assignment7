# -*- coding: utf-8 -*-
"""
Homework 7
Module 4
Mengfei Li
"""

import numpy as np
import matplotlib.pyplot as plt


def program4():
    N_max=50
    some_threshold=50
    #set up grid
    x,y=np.ogrid[-2:1:500j,-1.5:1.5:500j]
    c=x+1j*y
    
    #get z values
    z=c
    for v in range(N_max):
        z=z**2+c
 
    mask=abs(z)<some_threshold
    
    
    print '-----------Question 4----------'   
    #graph
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
  