"""
Write a program to print the maximum of sub array of size k.
"""


def maxOfSubarrayK(numbers, n, k):
    for i in range(n - k + 1):
        print(max(numbers[i:i + k]), end=' ')


if __name__ == '__main__':
    numbers = list(map(int, input('Enter the elements in array: ').strip(' ').split(' ')))
    n = len(numbers)
    k = int(input('Enter k vaue: '))
    maxOfSubarrayK(numbers, n, k)
