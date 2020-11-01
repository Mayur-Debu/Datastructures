'''
Write a program to remove duplicate characters from the string.
'''


def removeDuplicates(userInputString):
    for character in userInputString:
        if userInputString.count(character) > 1:
            continue
        else:
            print(character, end='')


if __name__ == '__main__':
    userInputString = input('Enter the string: ')
    removeDuplicates(userInputString)
