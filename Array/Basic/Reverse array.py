# Write a program to reverse the array.

def reverse(arr):
    print(arr[::-1])

if __name__ == '__main__':
    n=int(input('Enter the limit: '))
    arr=[None]*n
    arr=list(map(int,input().split(" ")))
    reverse(arr)