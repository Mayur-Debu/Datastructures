'''
Write a program to check whether one string is a rotation of another.
'''


def checkRotation(string1, string2):
    tempString = string1 + string1
    if string2 in tempString:
        return 1
    else:
        return -1


if __name__ == '__main__':
    string1, string2 = input('Enter two strings: ').strip(' ').split(' ')
    print(checkRotation(string1, string2))
