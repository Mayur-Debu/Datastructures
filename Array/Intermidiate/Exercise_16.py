'''
Write a program to find the longest consecutive subsequence.
'''


def longest_consecutive_subsequence(arr):
    consecutive_subsequence = set()
    arr = sorted(arr).copy()
    for i in range(len(arr)):

        if i == len(arr) - 1:

            if arr[i] - 1 == arr[i - 1]:
                consecutive_subsequence.add(arr[i])

            else:
                break

        elif i == 0:

            if arr[i] + 1 == arr[i + 1]:
                consecutive_subsequence.add(arr[i])

        else:

            if arr[i] + 1 == arr[i + 1] and arr[i] - 1 == arr[i - 1]:
                consecutive_subsequence.add(arr[i])

            else:
                consecutive_subsequence.add(arr[i])
                break

    print(consecutive_subsequence)
    return len(consecutive_subsequence)


if __name__ == '__main__':
    arr = []
    arr = list(map(int, input('Enter the elements in the array: ').strip().split()))
    print(longest_consecutive_subsequence(arr))
