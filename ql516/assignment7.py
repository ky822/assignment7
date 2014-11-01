# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 15:13:25 2014

@author: LaiQX
"""

import question1,question2,question3,question4

def main():
    print """===================================
            question1
==================================="""    
    question1.main()
    print """===================================
            question2
==================================="""
    question2.main()
    print """===================================
            question3
==================================="""
    question3.main()
    print """===================================
            question4
==================================="""
    try:
        question4.mandelbrot()
    except:
        pass
    
if __name__ == "__main__":
    main()