""" Implement the selection sort."""


def selectionSort(A):
    for i in range(len(A)):

        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    print("Sorted array")
    for i in range(len(A)):
        print("%d" % A[i]),


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    selectionSort(arr)
