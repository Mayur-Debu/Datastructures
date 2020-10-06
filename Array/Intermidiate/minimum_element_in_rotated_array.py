'''
Find the minimum element in an sorted and rotated array
'''

def minimum_element(arr):
    start=0
    end=len(arr)-1

    while(True):

        mid=(start+end)//2
        if (arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]):
            return arr[mid]
        elif (arr[mid-1]<arr[mid]):
            end=mid-1
        elif (arr[mid+1]<arr[mid]):
            start=mid+1

if __name__ == '__main__':
    arr=[]
    arr=list(map(int,input().strip(" ").split(" ")))
    # arr=sorted(arr).copy()
    print(minimum_element(arr))
