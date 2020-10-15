"""
Write a program to implement the queue using array and perform following operations
    1: Enqueue
    2: Dequeue
    3: Peek
    4: Display
"""

class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.front=0
        self.rear=0

    def enqueue(self):
        if self.rear<len(self.queue):
            if self.queue[self.rear]==None:
                self.queue[self.rear]=int(input('Enter the element in queue: '))
                self.rear+=1
            else:
                print('Queue overflow')

        elif self.rear==len(self.queue):
            self.rear=0
            if self.queue[self.rear]==None:
                self.queue[self.rear]=int(input('Enter the element in queue: '))
                self.rear+=1
            else:
                print('Queue Overflow')

    def dequeue(self):
        if self.front<len(self.queue):
            if self.queue[self.front]==None:
                print('Queue Underflow')
            else:
                print(f'The popped element from the queue is {self.queue[self.front]}')
                self.queue[self.front]=None
                self.front+=1

        elif self.front==len(self.queue):
            self.front=0
            if self.queue[self.front]==None:
                print('Queue Underflow')
            else:
                print(f'The popped element from the queue is {self.queue[self.front]}')
                self.queue[self.rear]==None
                self.front+=1


    def peek(self):
        if self.queue[self.front]==None:
            print('Nothing at peak')
        else:
            print(f'The peak element of the queue will be {self.queue[self.front]}')

    def display(self):
        pass

if __name__ == '__main__':
    circularQueueObject=CircularQueue(int(input('Size of queue: ')))

    while(True):
        print('1: Enqueue')
        print('2: Dequeue')
        print('3: Peek')
        print('4: Display')
        choice=int(input('Enter your choice: '))

        if choice==1:
            circularQueueObject.enqueue()
        elif choice==2:
            circularQueueObject.dequeue()
        elif choice==3:
            circularQueueObject.peek()
        elif choice==4:
            circularQueueObject.display()
        else:
            print('Error: Wrong Choice Made!!!')

