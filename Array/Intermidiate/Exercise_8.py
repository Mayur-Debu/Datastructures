'''
Find the first repeating element in the array of integers.
'''


def repeating_element(array):
    for i in range(len(array)):
        if array[i] in range(i + 1, len(array)):
            return array[i]

    else:
        return f'No Repeating Elements'


if __name__ == '__main__':
    array = []
    array = list(map(int, input().strip(" ").split(" ")))
    print(repeating_element(array))
