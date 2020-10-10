'''
You	are	given	a	list	of	n-1	integers	and	these	integers	are	in	the	range
of	1	to	n.	There	are	no	duplicates	in	the	list.	One	of	the	integers	is
missing	in	the	list.	Write	an	efficient	code	to	find	the	missing	integer.

'''


def findMissingElement(arr, n):
    # efficient approach to find the missing element
    temp = n * (n + 1) // 2
    return temp - sum(arr)


if __name__ == '__main__':
    n = int(input('Enter the value of n: '))
    arr = list(map(int, input('Enter the elements in the array: ').strip(' ').split(' ')))
    print(findMissingElement(arr, n))
