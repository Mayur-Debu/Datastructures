'''
Write a progam to check whether two string are anagram or not.
'''


def checkAnagram(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    if set1 == set2:
        for element in set1:
            if string1.count(element) == string2.count(element):
                return 0
        else:
            return -1
    else:
        return -1


if __name__ == '__main__':
    string1, string2 = input('Enter string').strip(' ').split(' ')
    print(checkAnagram(string1, string2))
