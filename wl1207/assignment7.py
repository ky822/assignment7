import  question1, question2, question3, question4

def main():
    for module in [question1, question2, question3, question4]:
        try:
            module.function()
        except(KeyboardInterrupt, EOFError):
            print "quit"
            break
            
if __name__ =='__main__':
    main()
