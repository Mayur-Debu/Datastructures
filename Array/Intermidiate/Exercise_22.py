'''
Minimum number of jumps to reach the end.
'''


def minimum_jumps(arr, n):
    position = 0
    maximum_jump = 0
    jump = 0

    if (n == 1):
        if (arr[0] == 0):
            return 0
        else:
            return 1

    while (position < n-1):

        if (position < n):
            maximum_jump = max([arr[0], arr[position]])
            position = position + maximum_jump
            jump += 1

    return jump


if __name__ == '__main__':
    arr = [1,3,5,8,9,2,6,7,6,8,9]
    print(minimum_jumps(arr, len(arr)))
