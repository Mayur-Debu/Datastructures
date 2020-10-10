'''
Given an array of size n and a number k , find all elements that appears more than n\k times.
'''


def check_occurance(arr, occurance_of_number):
    for i in range(len(arr)):
        count = arr.count(arr[i])
        if count == occurance_of_number:
            return arr[i]


if __name__ == '__main__':
    n = int(input('Enter number of elements: '))
    arr = [None] * n
    k = int(input('ENter the value of k: '))
    occurance_of_number = n // k
    arr = list(map(int, input('Enter the elements in array:  ').strip(" ").split(" ")))
    print(check_occurance(arr, occurance_of_number))
