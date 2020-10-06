'''
Write a progam to check whether two string are anagram or not.
'''


def checkAnagram(string1, string2):
    if len(string1) == len(string2):
        if ([char1 for char1 in set(string1)] == [char2 for char2 in set(string2)]):
            if ([string1.count(char1) for char1 in set(string1)] == [string2.count(char2) for char2 in set(string2)]):
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'
    else:
        return 'No'


if __name__ == '__main__':
    string1, string2 = input('Enter string').strip(' ').split(' ')
    print(checkAnagram(string1, string2))
