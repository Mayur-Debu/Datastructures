'''Find	Largest	sum	contiguous	Subarray.[Very	Important]'''
def largest_sum_contiguous_subarray(arr):
    max_so_far=0
    max_now=0
    for i in range(len(arr)):
        max_so_far+=arr[i]
        if(max_so_far<0):
            if(max_so_far<0 and i==len(arr)-1):
                arr=sorted(arr).copy()
                return arr[-1]
            else:
                max_so_far=0
        if(max_so_far>max_now):
            max_now=max_so_far
    return max_now




if __name__ == '__main__':
    n=int(input('Enter the limit of array'))
    arr=[None]*4
    arr=list(map(int,input('Enter the elements in array: ').strip(" ").split(" ")))
    print(largest_sum_contiguous_subarray(arr))