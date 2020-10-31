'''
Write a program to count the number of occurrences of each character in a string and print it.
'''


def occurancesOfCharacter(userInputString):

    for character in userInputString:
        print(f'{character} : {userInputString.count(character)}')


if __name__ == '__main__':
    userInputString = input('enter a string:')
    occurancesOfCharacter(userInputString)
