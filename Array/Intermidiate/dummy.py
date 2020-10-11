'''
2d array

'''



if __name__ == '__main__':
    row=int(input('Enter the number of rows: '))
    columns=int(input('Enter the number of columns: '))
    arr=[[None]*columns]*row
    arr=[[int(input('enter the element: '))for j in range(columns)]for i in range(row)]
    for r in arr:
        for c in r:
            print(c,end=' ')
        print()