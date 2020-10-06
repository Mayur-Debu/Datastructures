'''
GCD  of a given index in an array
'''


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b,a%b)

if __name__ == '__main__':
    arr=list(map(int,input('Enter the elements in array: ').strip(" ").split(" ")))
    gcd_set=[]
    i=0
    while(i<len(arr)-2):
        gcd_set.append((arr[i],arr[i+2]))
        i+=1
    result_array=[]
    for gcd_pair in gcd_set:
        print(gcd(gcd_pair[0],gcd_pair[1]))
