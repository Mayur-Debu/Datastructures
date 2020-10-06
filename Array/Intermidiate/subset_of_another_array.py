'''
Find whether an array is a subset of another array
'''


def subset(main_array, sub_array):

    for i in sub_array:
        if i in main_array:
            continue
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    main_array = []
    sub_array = []

    main_array = list(map(int, input('Enter the elements in main array: ').strip(' ').split(' ')))
    sub_array = list(map(int, input('Enter the elements in sub array: ').strip(' ').split(' ')))

    if subset(main_array, sub_array) == True:
        print('yes arr2[] is a subset of array1[]')

    else:
        print('No arr2[] is a subset of array1[]')
