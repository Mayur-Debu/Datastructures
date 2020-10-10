'''
Write a program to find the largest three elements in the array
'''


def largestThreeElements(arr):
    if len(arr) < 3:
        return -1

    first = second = third = 0
    for item in arr:

        if item > first:
            third = second
            second = first
            first = item

        elif item > second:
            third = second
            second = item

        elif item > third:
            third = item

    return f'the largest three elements are {first, second, third}'


if __name__ == '__main__':
    arr = list(map(int, input('Enter the elements: ').strip(' ').split(' ')))
    print(largestThreeElements(arr))
