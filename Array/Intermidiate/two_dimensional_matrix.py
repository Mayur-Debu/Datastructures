'''
Create a N * M matrix and take input from the user to populate it and then print the matrix
'''

rows=int(input('Enter the rows: '))
columns=int(input('Enter the columns: '))
arr=[[None]*columns]*rows

arr=[[int(input(f'Enter value at [{i},{j}]: ')) for j in range(columns)] for i in range(rows)]

for r in arr:
    for c in r:
        print(c,end=' ')
    print(' ')

