'''
. Find	all	pairs	on	integer	array	whose	sum	is	equal	to	given	number.
'''


def array_of_elements(arr):
    sum_array=[]
    sum_number=int(input('Enter the sum you want to search: '))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                pass
            elif(arr[i]+arr[j]==sum_number):
                sum_array.append((arr[i],arr[j]))
    return tuple(sum_array)

if __name__ == '__main__':
    arr=[]
    arr=list(map(int,input().split(" ")))
    print(array_of_elements(arr))