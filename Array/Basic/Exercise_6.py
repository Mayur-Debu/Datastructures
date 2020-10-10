'''
Write a program to find K largest and K smallest element in the array.
'''


def k_largest_k_smallest(arr, k):
    temp = sorted(arr)
    print(f'K smallest Value: {temp[:k + 1][k - 1]}')
    print(f'K largest Value: {temp[-k]}')


if __name__ == '__main__':
    n = int(input('Enter the n value: '))
    arr = [None] * n
    arr = list(map(int, input().split(" ")))
    k = int(input('Enter the k Value: '))
    k_largest_k_smallest(arr, k)
