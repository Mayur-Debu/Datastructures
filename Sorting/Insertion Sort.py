""" Implement the insertion sort."""


def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        while i > 0:
            if current < arr[i - 1]:
                arr[i] = arr[i - 1]
                arr[i - 1] = current
            i = i - 1
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter the numbers(1 2 3) :').strip(' ').split(' ')))
    print(insertionSort(arr))
