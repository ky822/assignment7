'''


@author: jiminzi
'''

import matplotlib.pyplot as plt
from numpy import *

def Question4():
    print 'question 4'
    #set the grid of x and y
    mandelbrot_set=compute_mandeohrot(50,50, 501,501 )
    plt.imshow(mandelbrot_set.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    #c=x+1j*y
    #z=c
   # for v in range(N_max):
        #z=z**2+c
def compute_mandeohrot(N_max,some_threshold,nx,ny):
    #seterr(all='warn')-- try to clean warnning
    x=linspace(-2,1,nx)
    y=linspace(-1.5,1.5,ny)
    c=x[:,newaxis]+1j*y[newaxis,:]
    z=c
    for v in xrange(N_max):
        z=z**2 + c
    # 2-d mask
    mandelbrot_set=(abs(z)<some_threshold)
    return mandelbrot_set   
if __name__ == '__main__':
    Question4()