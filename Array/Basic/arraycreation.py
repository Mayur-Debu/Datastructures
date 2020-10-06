'''1)Create an Array of size 10 of integers.
 Take input from the user for these 10 elements and print the entire array after that.'''

arr=[]
[arr.append(input()) for _ in range(10)]
print(arr)