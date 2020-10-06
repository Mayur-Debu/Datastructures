'''
Write a program to count the number of occurances if each character in a string and print it.
'''


def occurancesOfCharacter(userInputString):
    uniqueCharacter = []

    # Seperate the unique charecters
    for character in userInputString:
        if character in uniqueCharacter:
            continue
        else:
            uniqueCharacter.append(character)

    # Check occurrences of character in userInputString
    for character in uniqueCharacter:
        print(f'The {character} in {userInputString} occurred {userInputString.count(character)} times')


if __name__ == '__main__':
    userInputString = input('enter a string:')
    occurancesOfCharacter(userInputString)
