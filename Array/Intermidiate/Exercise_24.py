'''
Write a program to find a triplet that sums to a given value.
'''


def find_triplet(arr, n, actual_sum):
    arr = sorted(arr).copy()

    for i in range(n):
        l = i + 1
        r = n - 1

        while (l < r):
            if (arr[i] + arr[l] + arr[r] == actual_sum):
                print('[', arr[i], arr[l], arr[r], ']')
                return True

            elif (arr[i] + arr[l] + arr[r] < actual_sum):
                l += 1

            elif (arr[i] + arr[l] + arr[r] > actual_sum):
                r -= 1

    return False


if __name__ == '__main__':
    arr = []
    arr = list(map(int, input('Enter the values in array: ').strip(" ").split(" ")))
    actual_sum = int(input('Enter the sum to find triplet of: '))
    if (find_triplet(arr, len(arr), actual_sum) == True):
        print('1')
    else:
        print('0')
