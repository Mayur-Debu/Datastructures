'''
Write a program each word in the given string.
'''
def reverseEachWordInString(userInputString):
    stack=[]
    for charecter in range(len(userInputString)):
        if userInputString[charecter]==' ':
            print( ''.join(stack[::-1]),end=' ')
            stack=[]
        else:
            stack.append(userInputString[charecter])

    print(''.join(stack[::-1]))





if __name__ == '__main__':
    userInputString=input('Enter a string: ').strip(' ')
    reverseEachWordInString(userInputString)