def rearrange(arr):
    pivot=-1
    for i in range(len(arr)):
        if(arr[i]<0):
            pivot+=1
            arr[pivot],arr[i]=arr[i],arr[pivot]

    negative=0
    postive=pivot+1

    while(negative!=postive):
        if(arr[negative]<0):
            arr[negative],arr[postive]=arr[postive],arr[negative]
            negative+=2
            postive+=1

    return arr

if __name__ == '__main__':
    arr=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    # arr=list(map(int,input('Enter the elements in array: ').strip(" ").split(" ")))
    print(rearrange(arr))