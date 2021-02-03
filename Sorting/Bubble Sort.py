""" Implement the bubble sort."""


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter the elements in the array: ').strip(' ').split(' ')))
    print(bubbleSort(arr))
