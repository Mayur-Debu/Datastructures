'''
Write a program to find the first non-repeating element in the array.
'''


def first_non_repeating_no(arr):
    n = len(arr)
    for i in range(n):
        if arr.count(arr[i]) == 1:
            print(f'The first non repeating element is {arr[i]}')
            break
    else:
        print('-1')


if __name__ == '__main__':
    arr = []
    arr = list(map(int, input('Enter the elements in the array: ').strip(" ").split(" ")))
    first_non_repeating_no(arr)
