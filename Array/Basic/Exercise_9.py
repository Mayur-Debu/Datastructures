'''
Find the range of the array. Range means the difference between the maximum and minimum element in the array.
'''


def difference(arr):
    arr = sorted(arr).copy()
    return (arr[-1] - arr[0])


if __name__ == '__main__':
    n = int(input('Enter the n value: '))
    arr = [None] * n
    arr = list(map(int, input().split(" ")))
    print(difference(arr))
