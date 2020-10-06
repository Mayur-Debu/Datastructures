'''
Find the two repetative elements given in the array
'''

def repetative_elements(arr,n):
    repeated_elements=[]
    pointer=0
    arr=sorted(arr).copy()
    while(pointer!=n):
        if(arr[pointer] in arr[pointer+1:]):
            repeated_elements.append(arr[pointer])
        pointer+=1
    return f'Repeated elements are: {repeated_elements}'

if __name__ == '__main__':
    n=int(input('Enter the limit of array'))
    arr=[None]*n
    arr=list(map(int,input('Enter the values: ').strip(" ").split(" ")))
    print(repetative_elements(arr,len(arr)))
