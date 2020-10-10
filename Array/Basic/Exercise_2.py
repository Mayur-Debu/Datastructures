'''
Check whether a element entered by a user is present in the array or not.
'''


def search_in_array(arr):
    element = int(input('enter the number to search: '))
    for i in range(len(arr)):
        if element == arr[i]:
            return True
    else:
        return False


if __name__ == '__main__':
    n = int(input('enter the limit: '))
    arr = [None] * n
    arr = list(map(int, input().split(" ")))
    print(search_in_array(arr))
