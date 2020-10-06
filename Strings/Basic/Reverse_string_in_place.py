'''
Write the program to reverse a string in place
'''


def reverseString(string):
    print(f'Method 1 slicing: {string[::-1]}')

    reverseString = []
    for character in string[::-1]:
        reverseString.append(character)

    print('Method 2 Userdefined: ', end='')
    for character in reverseString:
        print(character, end='')


if __name__ == '__main__':
    userInputString = input('Enter a string')
    reverseString(userInputString)
