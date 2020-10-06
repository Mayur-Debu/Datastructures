'''
Find common elements in three sorted array's.
'''

def common_element(array_1,array_2,array_3):
    array_1=sorted(array_1).copy()
    array_2=sorted(array_2).copy()
    array_3=sorted(array_3).copy()
    return f'Common elements in 3 sorted array\'s are: {set(array_1)&set(array_2)&set(array_3)}'




if __name__ == '__main__':
    array_1=list(map(int,input('Enter elements in array 1: ').strip(" ").split(" ")))
    array_2=list(map(int,input('Enter elements in array 2: ').strip(" ").split(" ")))
    array_3=list(map(int,input('Enter elements in array 3: ').strip(" ").split(" ")))

    print(common_element(array_1,array_2,array_3))