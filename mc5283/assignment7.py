import answer1,answer2,answer3,answer4

def main():
    for module in [answer1, answer2,answer3,answer4]:
        module.run()
        try:
            raw_input('Press enter to continue \n')
        except (KeyboardInterrupt, EOFError):
            print 'Terminated'
            break


if __name__ == '__main__':
    main()
