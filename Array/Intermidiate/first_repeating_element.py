'''
Find the first repeating element in the array of integers.
'''
def repeating_element(array):
  for i in range(len(array)):
      for j in range(len(array)):
          if i==j:
              pass
          elif array[i]==array[j]:
              return f'First repeating element is : {array[i]}'

  else:
      return f'No Repeating Elements'


if __name__ == '__main__':
    array=[]
    array=list(map(int,input().strip(" ").split(" ")))
    print(repeating_element(array))