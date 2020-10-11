'''
Write a program to find median in a row wise sorted array.
'''


def median_of_matrix(arr):
    arr = [item for sub_array in arr for item in sub_array]
    arr.sort()
    median = arr[len(arr) // 2]
    return median


if __name__ == '__main__':
    rows = int(input('Rows: '))
    columns = int(input('columns: '))
    arr = [[None] * columns] * rows
    arr = [[int(input(f'Enter the element at[{j},{i}]')) for i in range(columns)] for j in range(rows)]
    for r in arr:
        for c in r:
            print(c, end=" ")
        print(" ")
    print(f'The median in the sorted matrix is : {median_of_matrix(arr)}')
