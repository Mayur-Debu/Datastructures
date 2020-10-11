'''
Write a program to find the maximum number of one's.
'''
rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))

arr = [[None] * columns] * rows
arr = [[int(input(f'Enter the element at [{j},{i}]: ')) for i in range(columns)] for j in range(rows)]

for r in arr:
    for c in r:
        print(c, end=' ')
    print(' ')

print(f'Row {(arr.index(max(arr))) + 1} contains maximum number of 1')
