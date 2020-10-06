'''
Write a program to check whether one string is a rotation of another.
'''


def checkForRotation(userInputString1, userInputString2):
    while (userInputString1 != userInputString2):
        userInputString1 = userInputString1 * 2
        if userInputString2 in userInputString1:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    userInputString1, userInputString2 = input('Enter two string\'s: ').strip(' ').split(' ')
    print(checkForRotation(userInputString1, userInputString2))
