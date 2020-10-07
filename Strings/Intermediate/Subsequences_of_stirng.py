'''
Write a program to print all the subsequences of a string
'''
def  printSubsequence(inputString,outputString):
    if(len(inputString)==0):
        print(outputString,end=' ')
    else:
        printSubsequence(inputString[1:],outputString)
        printSubsequence(inputString[1:],outputString+inputString[0])



if __name__ == '__main__':
    inputString=input()
    outputString=""
    # print(inputString[1:])
    printSubsequence(inputString,outputString)