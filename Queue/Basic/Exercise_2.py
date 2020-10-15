"""
Write a program to implement the circular queue using array and perform following operations
    1: Enqueue
    2: Dequeue
    3: Peek
    4: Display
"""


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0

    def enqueue(self):
        if self.queue[self.rear] == None:
            self.queue[self.rear] = int(input('Enter the element in array'))
            self.rear = (self.rear + 1) % len(self.queue)
        else:
            print('Cirular Queue Overflow')

    def dequeue(self):
        if self.queue[self.front] == None:
            print('Circular Queue Underflow')
        else:
            print(f'The popped element from the circular queue is {self.queue[self.front]}')
            self.queue[self.front] = None
            self.front = (self.front + 1) % len(self.queue)

    def peek(self):
        if self.queue[self.front] == None:
            print('Nothing to display ')
        else:
            print(f'The peak element of the circular string is {self.queue[self.front]}')

    def display(self):
        for item in self.queue:
            if item == None:
                break
            else:
                print(f'|| {item}', end=" ")
            print()


if __name__ == '__main__':
    circularQueueObject = CircularQueue(int(input('Size of queue: ')))

    while (True):
        print('1: Enqueue')
        print('2: Dequeue')
        print('3: Peek')
        print('4: Display')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            circularQueueObject.enqueue()
        elif choice == 2:
            circularQueueObject.dequeue()
        elif choice == 3:
            circularQueueObject.peek()
        elif choice == 4:
            circularQueueObject.display()
        else:
            print('Error: Wrong Choice Made!!!')
