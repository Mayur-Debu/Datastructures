'''
Write a program to check whether a string is palindrome or not.
'''

if __name__ == '__main__':
    userInputString = input('Enter a string')
    if userInputString[::] == userInputString[::-1]:
        print('Palindrome')
    else:
        print('-1')
