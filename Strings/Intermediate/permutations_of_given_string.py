'''
Write a programa to print all permutations of a given string.
'''

from itertools import permutations

if __name__ == '__main__':
    userInputString = input('Enter a string: ')
    Permutation = list(permutations(userInputString))
    i = 0
    for item in Permutation:
        i += 1
        print(i, ''.join(item))
