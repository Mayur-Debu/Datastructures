'''
Given	an	array	which	consists	of	only	0,	1	and	2.	Sort	the	array	without
using	any	sorting	algorithm.
'''

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            else:
                pass
    return arr

if __name__ == '__main__':
    n=int(input('enter the value of n: '))
    arr=[None]*n
    arr=list(map(int,input().split(" ")))
    print(sort(arr))