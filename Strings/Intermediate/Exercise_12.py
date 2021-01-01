""" Find the longest common subsequence in two strings."""


def commomSubsequence(str1, str2):
    counter = 0
    for letter in str1:
        if letter in str2:
            counter += 1
        else:
            continue
    return counter


if __name__ == '__main__':
    str1 = input('Enter the first string: ')
    str2 = input('Enter the second string: ')

    str1 = str1.upper()
    str2 = str2.upper()

    print(commomSubsequence(str1, str2))
