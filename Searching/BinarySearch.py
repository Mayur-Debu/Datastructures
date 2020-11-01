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


print(binary_search([1, 2, 4, 5, 3], 3))
