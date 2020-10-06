'''
Minimize the maximum difference between the heights
'''


def minimum_difference(arr, n, k):
    # for single element array
    if (n == 1):
        return 0

    # sort array
    arr = sorted(arr).copy()
    ans = arr[n - 1] - arr[0]

    # handle corner elements
    small = arr[0] + k
    big = arr[n - 1] - k

    if small > big:
        small, big = big, small

    # traverse middle element
    for i in range(1, n - 1):

        add = arr[i] + k
        subtract = arr[i] - k

        if subtract >= small or add <= big:
            continue

        if big - subtract <= add - small:
            small = subtract
        else:
            big = add

    return min(ans, big - small)


if __name__ == '__main__':
    arr = list(map(int, input('Enter element in the array: ').strip(" ").split(" ")))
    k = int(input('Enter the value of k: '))
    print(f'The Maximum difference is: {minimum_difference(arr, len(arr), k)}')
