"""
Find the occurrence of n in arr of size m.
"""

def occurences_of_n(arr,n):
    return f'The occurencecs {n} in array are {arr.count(n)}'

if __name__ == '__main__':
    arr=list(map(int,input().strip(' ').split(' ')))
    n=int(input('Enter the n: '))
    print(occurences_of_n(arr,n))