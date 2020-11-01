'''
Write a program to the longest repeated subsequence.
'''

def longestRepeatedSubsequence(string):
    stringSet=[]
    lrs=[]
    for character in string:
        if character in stringSet:
            continue
        else:
            stringSet.append(character)

    for character in stringSet:
        if string.count(character)>1:
            lrs.append(character)
        else:
            continue
    return ''.join(lrs),len(lrs)

if __name__ == '__main__':
    userInputString=input('Enter a string: ')
    print(longestRepeatedSubsequence(userInputString))