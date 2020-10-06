def largest_three(arr):
    arr=sorted(arr,reverse=True).copy()
    print(f'The largest three element\' are: {[arr[i] for i in range(3)]}')

if __name__ == '__main__':
    arr=[]
    arr=list(map(int,input('Enter the values in array: ').strip(" ").split(" ")))
    largest_three(arr)