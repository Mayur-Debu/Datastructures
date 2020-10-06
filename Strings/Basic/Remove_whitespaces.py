'''
Write a program to remove all whitespaces in a given string.
'''


def removeWhiteSpaces(userInputString):

    for character in userInputString:
        if character == ' ':
            userInputString = userInputString.replace(i, '')
    return userInputString


if __name__ == '__main__':
    userInputString = input('Enter a string: ')
    print(removeWhiteSpaces(userInputString))
