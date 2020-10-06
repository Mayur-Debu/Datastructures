def first_non_repeating_no(arr):
    n=len(arr)
    for i in range(n):
        j=0
        while(j<n):
            if i!=j and arr[i]==arr[j]:
                break
            j+=1
        if (j == n):
            print(f'first non repeating element is: {arr[i]}')
            break
    else:
        print('-1')


if __name__ == '__main__':
    arr=[]
    arr=list(map(int,input('Enter the elements in the array: ').strip(" ").split(" ")))
    first_non_repeating_no(arr)