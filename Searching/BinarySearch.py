"""Implement the binary search using array."""


def binary_search(a, key):
    '''The Array Has to be Sorted'''
    a = sorted(a)
    low = 0
    high = len(a) - 1
    while low < high:
        mid = (low + high) // 2
        if key == a[mid]:
            return True
        elif key < mid:
            high = mid - 1
        else:
            low = mid + 1

    return False


if __name__ == '__main__':

    a = list(map(int, input('Enter the list of numbers: ').strip(' ').split(' ')))
    key = int(input('Enter the number to be searched: '))

    if binary_search(a, key):
        print('FOUND')
    else:
        print('NOT FOUND')
