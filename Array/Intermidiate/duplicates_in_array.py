'''
Find duplicates in array.
'''
def duplicate_element(arr):
    duplicate=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                pass
            elif arr[i]==arr[j]:
                duplicate.append(arr[i])
    return set(duplicate)

if __name__ == '__main__':
    arr=[]
    arr=list(map(int,input().strip(" ").split(" ")))
    print(f'Duplicates in the array\'s are: {duplicate_element(arr)}')