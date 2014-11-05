# -*- coding: utf-8 -*-

import numpy as np

# the question2

def main():
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    c = (a.T) / b
    print c.T
    
if __name__ == "__main__":
    main()
    
    