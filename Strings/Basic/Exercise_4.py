'''
Find the duplicate characters in the strings
'''


def findDuplicates(userInputString):
    uniqueCharacter = set(userInputString)
    for character in uniqueCharacter:
        if userInputString.count(character) > 1:
            print(f'{character}: {userInputString.count(character)}')


if __name__ == '__main__':
    userInputString = input('Enter the string: ')
    findDuplicates(userInputString)
