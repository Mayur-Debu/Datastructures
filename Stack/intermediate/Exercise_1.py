"""
Implement stack using queues.
"""


class StackUsingQueue:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.rear = -1
        self.front = -1

    def push(self):

        if self.rear == self.size - 1:
            print(f'The stack\'s overflow')
        else:
            self.rear += 1
            self.front += 1
            self.stack[self.rear] = int(input('Enter the element to push'))

    def pop(self):
        if self.rear == self.front == -1:
            print(f'The stack\'s overflow')
        else:
            print(f'The popped element from the stack is {self.stack[self.front]}')
            self.front -= 1
            self.rear -= 1

    def display(self):
        if self.front == -1:
            print(f'The stack\'s empty')

        for data in self.stack:
            print(data, end=' || ')
        print()


if __name__ == '__main__':
    try:
        n = int(input('Enter the size of stack: '))
        s = StackUsingQueue(n)
        while 1:
            print('1: Push')
            print('2: Pop')
            print('3: Display')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                s.push()
            elif choice == 2:
                s.pop()
            elif choice == 3:
                s.display()
            else:
                print('Error 404: Request not found.')

    except ValueError as v:
        print('Enter A Number')
