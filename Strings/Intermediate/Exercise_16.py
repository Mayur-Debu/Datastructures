""" Find next greater number with the same number of digits """

from itertools import permutations

def nextGreaterNumber(permutations,Number):
    Number=''.join(map(str,Number))
    for permutation in permutations:
        permutation=''.join(map(str,permutation))
        if permutation>Number:
            return permutation
        else:
            continue
    else:
        return sorted(Number)



if __name__ == '__main__':
    Number=list(map(int,input('Enter the Number to find the next greater number of: ')))
    permutation=permutations(Number)
    print(nextGreaterNumber(permutation,Number))

