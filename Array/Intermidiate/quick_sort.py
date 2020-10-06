'''
Sort a given ARRAY using the quick sort algorithm
'''


def partition(arr,low,high):
    i=(low - 1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)



def quicksort(arr,low,high):
    if low < high:
        pi=partition(arr,low,high)
        quicksort(arr,low,high-1)
        quicksort(arr,pi+1,high)







if __name__ == '__main__':
    arr=[]
    arr=list(map(int,input('Enter the elements in the array: ').strip(" ").split(" ")))
    n=len(arr)
    quicksort(arr,0,n-1)
    for i in range(n):
        print(arr[i])
