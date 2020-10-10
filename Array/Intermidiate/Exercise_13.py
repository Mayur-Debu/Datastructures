'''Find	Largest	sum	contiguous Subarray. [Very	Important]'''


def largest_sum_contiguous_subarray(arr):
    max_so_far = 0
    max_now = 0
    for item in arr:
        max_now += item
        if max_now < 1:
            max_now = 0
        elif max_now > max_so_far:
            max_so_far = max_now
    if max_so_far == 0:
        return max(arr)
    else:
        return max_so_far


if __name__ == '__main__':
    n = int(input('Enter the limit of array'))
    arr = [None] * 4
    arr = list(map(int, input('Enter the elements in array: ').strip(" ").split(" ")))
    print(largest_sum_contiguous_subarray(arr))
