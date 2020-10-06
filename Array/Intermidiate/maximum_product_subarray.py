'''
Find the maxuimum product subarray
'''
def max_product_subarray(arr):
    max_product=1
    max_now=arr[0]
    for i in range(len(arr)):
        max_product=max_product*arr[i]
        if(max_product>max_now):
            max_now=max_product
    return max_now


if __name__ == '__main__':
    arr=list(map(int,input('Enter the elements in array: ').strip().split()))
    print(max_product_subarray(arr))