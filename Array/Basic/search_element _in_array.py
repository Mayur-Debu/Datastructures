'''
Check whether n is present in an array of size m or not.
Input -n,m (Input number, size of array)-Take input n elements for the arrayOutput -> true/false
'''

def search_in_array(arr):
    element=int(input('enter the number to search: '))
    for i in range(len(arr)):
        if element==arr[i]:
            return True
    else:
        return False

if __name__ == '__main__':
    n=int(input('enter the limit: '))
    arr=[None]*n
    arr=list(map(int,input().split(" ")))
    print(search_in_array(arr))