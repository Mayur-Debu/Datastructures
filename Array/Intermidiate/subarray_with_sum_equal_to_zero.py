def subarray_with_sum_zero(arr):
    s=set()
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
        if sum==0  or sum in s:
            print(s)
            return True
        s.add(sum)

    return False

if __name__ == '__main__':
    arr=[4, 2, -3, 1, 6]
    if subarray_with_sum_zero(arr) == True:
        print('True')
    else:
        print('False')