'''
Write a program to find the duplicate in the array.
'''


def duplicateElements(arr):
    duplicateElement = []
    for item in arr:
        if arr.count(item) > 1:
            duplicateElement.append(item)
    return set(duplicateElement)


if __name__ == '__main__':
    arr = list(map(int, input().strip(" ").split(" ")))
    print(f'The duplicate elemetn\'s are: {duplicateElements(arr)}')
