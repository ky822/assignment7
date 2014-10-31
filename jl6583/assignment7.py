'''
Created on Oct 29, 2014

This is the main entrance to all the functionalities, 


@author: luchristopher
'''

from demos import *

def main():
    
    list_of_demos = [DemoOne(),DemoTwo(),DemoThree(),DemoThree(),DemoFour()]
    for demos in list_of_demos:
        demos.demoShow()
        

if __name__ == '__main__':
    main()