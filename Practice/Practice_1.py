"""
Input:
    2
    Hacker
    Rank
Output: 
    Hce akr
    Rn ak
"""

def printString(string):
    newstring1=[]
    newstring2=[]
    for word in string:
        for i in range(len(word)):
            if i%2==0:
                newstring1.append(word[i])
            else:
                newstring2.append(word[i])
        print(('').join(newstring1 + list(' ') + newstring2))
        newstring1=[]
        newstring2=[]

if __name__ == '__main__':
    no_of_element=int(input())
    string=[]
    for _ in range(no_of_element):
        string.append(input().strip(' '))

    printString(string)



