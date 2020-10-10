'''
Given a number n. find the number of occurrences of number n in the array.
'''


def occurances(arr, n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == n:
            count += 1
    return count


if __name__ == '__main__':
    arr = []
    arr = list(map(int, input('Enter the elements of array: ').strip(" ").split(" ")))
    n = int(input('Enter the number to find the occurance of: '))
    print(occurances(arr, n))
