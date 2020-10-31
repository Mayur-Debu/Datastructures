'''
Write the program to reverse a string in place
'''


def reverseString(string):
    print(f'Reversed String: {string[::-1]}')

if __name__ == '__main__':
    userInputString = input('Enter a string')
    reverseString(userInputString)
