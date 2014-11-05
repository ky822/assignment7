import sys
from questions import *
import numpy as np

def main():
    k = 1
    try:
        for module in [question1, question2, question3, question4]:
            qstr = 'Results for Question ' + str(k) + '? yes/no \n'
            if raw_input(qstr) == 'yes':
                module.result()
            k = k + 1
    except(KeyboardInterrupt):
        print 'Bye!'
        sys.exit()

if __name__ == '__main__':
    main()

