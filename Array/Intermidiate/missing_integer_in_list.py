'''
You	are	given	a	list	of	n-1	integers	and	these	integers	are	in	the	range
of	1	to	n.	There	are	no	duplicates	in	the	list.	One	of	the	integers	is
missing	in	the	list.	Write	an	efficient	code	to	find	the	missing	integer.

'''


def check_missing_value(arr):
    missing=[]
    for i in range(1,n+1):
        if (str(i) in arr):
            pass
        else:
            missing.append(i)
    return missing



if __name__ == '__main__':
    n=int(input('Enter the n value: '))
    arr=[None]*4
    for i in range(n):
        arr[i]=input(f'Enter the element at a[{i}]: ')
    print(f'The missing values are: {check_missing_value(arr)}')