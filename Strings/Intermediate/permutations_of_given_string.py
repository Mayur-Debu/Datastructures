'''
Write a programa to print all permutations of a given string.
'''


def getPermutation(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r):
            s[l], s[i] = s[i], s[l]
            getPermutation(s, l + 1, r)
            s[l], s[i] = s[i], s[l]  # bactrack to the previous step.


if __name__ == '__main__':
    string = list(input('Enter the string: '))
    getPermutation(string, 0, len(string))
