'''
Write a program to implement a stack with the following functions.

Functions:
            push()
            pop()
            peek()
            empty()
            search()
'''

class Stack:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*size
        self.top=-1


    def push(self):
        if self.top==self.size-1:
            print(f'Error: The stack is overflow!!!')
        else:
            self.top+=1
            self.arr[self.top]=int(input('Enter the value to push in stack: '))

    def pop(self):
        if self.top==-1:
            print(f'Error: The stack is underflow!!! ')
        else:
            print(f'The popped element from the stack is {self.arr[self.top]}')
            self.arr[self.top]=None
            self.top-=1

    def peek(self):
        if self.top==-1:
            print(f'Error: The stack is empty!!!')
        else:
            print(f'The peak element of the stack is {self.arr[self.top]}')

    def empty(self):
        if self.top==-1:
            print('The stack is empty. Ready to push element.')
        elif self.top<self.size-1:
            print('Stack is not empty. But still can push elements.')
        else:
            print('Error: The stack is not empty.')

    def search(self):
        if self.top==-1 :
            print('The stack is empty. Nothing to search in the stack.')
        else:
            search_item=int(input('Enter the value to search in the stack: '))
            for item in range(len(self.arr)):
                if self.arr[item]==search_item:
                    print(f'Searched item is present at {item+1}')
                    break
            else:
                print('Searched element is not in the array.')

    def display(self):
        for item in self.arr:
            print(f'|| {item} ',end='')
        print('||')



if __name__ == '__main__':
    stackobject=Stack(5)
    while(True):
        print('1.Push')
        print('2.Pop')
        print('3.Peek')
        print('4.Empty')
        print('5.Search')
        print('6.Display the stack')
        choice=int(input('Enter your choice: '))

        if choice==1:
            stackobject.push()
        elif choice==2:
            stackobject.pop()
        elif choice==3:
            stackobject.peek()
        elif choice==4:
            stackobject.empty()
        elif choice==5:
            stackobject.search()
        elif choice==6:
            stackobject.display()
        else:
            print('Error: You choose the wrong option!!!')
            print('Please try again!!!')




