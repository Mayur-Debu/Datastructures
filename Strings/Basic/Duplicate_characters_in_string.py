'''
Find the duplicate characters in the strings
'''


def findDuplicates(userInputString):
    uniqueCharacter = []
    for character in userInputString:
        if character in uniqueCharacter:
            continue
        else:
            uniqueCharacter.append(character)

    for character in uniqueCharacter:
        if userInputString.count(character) > 1:
            print(f'{character} is a duplicated charater.')
    else:
        print('-1')


if __name__ == '__main__':
    userInputString = input('Enter the string: ')
    findDuplicates(userInputString)
