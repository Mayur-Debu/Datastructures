'''
Rearrange the characters in the string such that two adjacent characters are not same.
'''

def distinctWindow(s):

    distinctWindowString=[]
    for i in range(len(s)):
        distinctWindowString = []
        for j in range(i,i+1):
            if j<=len(s):
                distinctWindowString.append(s[j])
            else:
                return  -1
    if set(s) in distinctWindowString:
        return ''.join(distinctWindowString)




if __name__ == '__main__':
    string=list(input('Enter the string: '))
    print(string)
    print(distinctWindow(string))