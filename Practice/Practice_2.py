rows=int(input())
columns=rows
arr=[[input() for _ in range(rows)] for _ in range(columns)]

for columns in arr:
    for rows in columns:
        print(int(rows),end=' ')
    print()