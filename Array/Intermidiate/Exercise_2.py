'''
Write a program to cyclically rotate a array one by one.
'''


def rotate(arr):
    n = len(arr)
    x = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = x
    return arr


if __name__ == '__main__':
    arr = []
    arr = list(map(int, input('Enter the elements in array: ').split(" ")))
    print(f'Rotated array: {rotate(arr)}')
