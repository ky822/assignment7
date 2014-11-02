'''
Created on Oct 31, 2014

@author: ds-ga-1007
'''
import answers.Question1, answers.Question2,answers.Question3,answers.Question4

def main():
    for module in [answers.Question1, answers.Question2,answers.Question3,answers.Question4]:
        module.main()
    
if __name__ == '__main__':
    main()