'''1)Create an Array of size 10 of integers. Take input from the user for these 10 elements and print the entire array after that.'''

if __name__ == '__main__':
    arr = list(map(int, input('Enter the elements of array: ').strip(' ').split(' ')))
    for item in arr:
        print(item, end=' ')
