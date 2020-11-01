'''
Write a program to check whether a string is a valid shuffle of two strings or not.
'''

from itertools import permutations


def checkForValidShuffle(string1, string2, shuffledString):
    Permutations = permutations(string1 + string2)

    if shuffledString in [''.join(item) for item in Permutations]:
        return True
    else:
        return False


if __name__ == '__main__':
    string1, string2, shuffledString = input('Enter 3 strings: ').strip(' ').split(' ')
    print(checkForValidShuffle(string1, string2, shuffledString))
