"""
write a program to implement the input restricted dequeue using the array and perform the following operations.
    1: Enqueue
        * Enqueue from only front
    2: Dequeue
        * Dequeue at front
        * Dequeue at rear
    3: isEmpty
    4: sizeOfDequeue
"""


class Dequeue:
    def __init__(self):
        self.dq = []

    def enqueue(self):
        self.dq.append((input('Enter the element: ')))

    def dequeueFront(self):
        print(f'The popped element from the front of the dequeue is {self.dq.pop()}')

    def dequeueRear(self):
        print(f'The popped element from the rear of the queue is {self.dq.pop(0)}')

    def isEmpty(self):
        if self.dq == []:
            print('The dequeue is empty.')
        else:
            print('Dequeue isn\'t empty.')

    def sizeOfDequeue(self):
        print(f'The size of the dequeue is {len(self.dq)}')


if __name__ == '__main__':
    dq = Dequeue()
    while True:
        print('1: Add element')
        print('2: Remove element from front')
        print('3: Remove element from rear')
        print('4: Check if dequeue is empty ')
        print('5: Size of dequeue')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            dq.enqueue()
        elif choice == 2:
            dq.dequeueFront()
        elif choice == 3:
            dq.dequeueRear()
        elif choice == 4:
            dq.isEmpty()
        elif choice == 5:
            dq.sizeOfDequeue()
        else:
            print('Error: Wrong choice, try again!!!')
