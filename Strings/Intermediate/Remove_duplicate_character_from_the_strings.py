'''
Write a program to remove duplicate characters from the string.
'''


def removeDuplicates(userInputString):
    manipulatedString = []
    userInputString = userInputString.lower()
    for charecter in userInputString:
        if userInputString.count(charecter) > 1:
            continue
        else:
            manipulatedString.append(charecter)

    if ''.join(manipulatedString) == userInputString:
        return None
    else:
        return ''.join(manipulatedString)


if __name__ == '__main__':
    userInputString = input('Enter the string: ')
    print(removeDuplicates(userInputString))
