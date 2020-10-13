"""
Write a program to implement two stacks in a array.
"""


class TwoStack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * self.size
        self.top1 = -1
        self.top2 = len(self.arr)

    def push1(self):
        if self.arr[self.top1 + 1] == None:
            self.top1 += 1
            self.arr[self.top1] = int(input('Enter the element in stack1: '))
        else:
            print('Stack1 overflow')

    def push2(self):
        if self.arr[self.top2 - 1] == None:
            self.top2 -= 1
            self.arr[self.top2] = int(input('Enter the element in stack2: '))
        else:
            print('Stack2 overflow')

    def pop1(self):
        if self.top1 == -1:
            print('Stack1 underflow')
        else:
            print(f'The popped element from the stack 1 is {self.arr[self.top1]}')
            self.arr[self.top1] = None
            self.top1 -= 1

    def pop2(self):
        if self.top2 == len(self.arr):
            print('Stack2 underflow')
        else:
            print(f'The popped element from the stack 2 is {self.arr[self.top2]}')
            self.arr[self.top2] = None
            self.top2 += 1

    def displayStack1(self):
        if self.top1 == -1:
            print('Nothing to display form stack 1')
        else:
            for item in self.arr[0:self.top1 + 1]:
                print(f' {item} || ', end='')
            print()

    def displayStack2(self):
        if self.top2 == len(self.arr):
            print('Nothing to display from stack 2')
        else:
            for item in self.arr[:self.top2 - 1:-1]:
                print(f' {item} || ', end='')
            print()


if __name__ == '__main__':
    twoStackObject = TwoStack(int(int(input('Enter the size of array: '))))
    while (True):
        print('1.Push in stack 1')
        print('2.Push in stack 2')
        print('3.Pop in stack 1')
        print('4.Pop in stack 2')
        print('5.Display elements in stack 1')
        print('6.Display elements in stack 2')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            twoStackObject.push1()
        elif choice == 2:
            twoStackObject.push2()
        elif choice == 3:
            twoStackObject.pop1()
        elif choice == 4:
            twoStackObject.pop2()
        elif choice == 5:
            twoStackObject.displayStack1()
        elif choice == 6:
            twoStackObject.displayStack2()
        else:
            print('Error: Wrong choice. Select a valid option.')
