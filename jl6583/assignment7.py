'''
Created on Oct 29, 2014

This is the main entrance to the project, shows the answer to
each questions one by one.


@author: luchristopher
'''

from demos import *

def main():
    '''Creates an demo instance for all 4 questions and show the answer following
        the requirements
    '''
    list_of_demos = [DemoOne(),DemoTwo(),DemoThree(),DemoThree(),DemoFour()]
    for demos in list_of_demos:
        demos.demoShow()
        

if __name__ == '__main__':
    main()