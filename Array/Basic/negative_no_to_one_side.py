'''
Move	all	the	negative	elements	to	one	side	of	the	array.
'''
#
def sort(arr):
    final_value=len(arr)
    i,j=0,0
    while(i!=final_value):
        if(arr[i]<0):
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
        else:
            i+=1
    return arr


if __name__ == '__main__':
    n=int(input('enter the value of n: '))
    arr=[None]*n
    arr=list(map(int,input().split(" ")))
    print(sort(arr))