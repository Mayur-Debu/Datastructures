"""
Write a program to print the maximum of sub array of size k.
"""


def maxOfSubarrayK(numbers,k):
    pass

if __name__ == '__main__':
    numbers=list(map(int,input('Enter the elements in array: ').strip(' ').split(' ')))
    k=int(input('Enter k vaue: '))
    print(maxOfSubarrayK(numbers,k+1))