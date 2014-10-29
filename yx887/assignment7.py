import question1, question2, question3, question4

def main():
    for module in [question1, question2, question3, question4]:
        module.run_program()
        try:
            raw_input('Press enter/return to continue ...\n')
        except (KeyboardInterrupt, EOFError):
            print 'Bye!'
            break

if __name__ == '__main__':
    main()
