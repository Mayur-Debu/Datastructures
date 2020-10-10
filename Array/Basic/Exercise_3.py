'''
Find the minimum and maximum element in an array.
'''


def largest(arr):
    large = 0
    for i in range(len(arr)):
        if (arr[i] > large):
            large = arr[i]
    return large


def smallest(arr):
    small = arr[-1]
    for i in range(len(arr)):
        if (arr[i] < small):
            small = arr[i]
    return small


if __name__ == '__main__':
    n = int(input('Enter the limit: '))
    arr = [None] * n
    arr = list(map(int, input().split(" ")))

    print(f'MAX:{largest(arr)}')
    print(f'MIN:{smallest(arr)}')
