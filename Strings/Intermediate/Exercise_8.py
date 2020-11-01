'''
Write a program to split the binary tree into substrings with equal 0's and 1's.
'''


def binarySubstring(string):
    zeroCount = 0
    oneCount = 0
    subStringCount = 0

    for i in range(len(string)):
        if (string[i] == "0"):
            zeroCount += 1
        elif (string[i] == "1"):
            oneCount += 1

    if zeroCount == oneCount:
        subStringCount += 1

    return subStringCount


if __name__ == '__main__':
    binaryString = input('Enter a binary string with 0\'s and 1\'s: ')
    print(binarySubstring(binaryString))
