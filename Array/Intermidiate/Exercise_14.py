'''
Find the factorial of large number.
'''


def factorial(largest_no):
    fact = 1
    for i in range(1, largest_no + 1):
        fact = fact * i
    return fact


if __name__ == '__main__':
    arr = []
    arr = list(map(int, input('Entee the elements of array: ').strip(" ").split(" ")))
    arr = sorted(arr, reverse=True).copy()
    print(arr)
    largest_no = arr[0]
    print(largest_no)
    print(f'The factorial of largest number in array is: {factorial(largest_no)}')
