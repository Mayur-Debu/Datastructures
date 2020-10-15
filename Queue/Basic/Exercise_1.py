"""
Write a program to implement queue using array with the following functions
    1: Enqueue
    2: Dequeue
    3: Peek
    4: Display
"""
class Queue:
    def __init__(self,size):
        self.size=size
        self.front=0
        self.rear=0
        self.queue=[None]*self.size

    def enqueue(self):
        if self.rear==len(self.queue):
            print('Queue Overflow')
        else:
            self.queue[self.rear]=int(input('Enter element in array: '))
            self.rear+=1

    def dequeue(self):
        if self.front==len(self.queue):
            print('Queue Underflow')
        else:
            if self.queue[self.front]==None:
                print('Nothing to pop')
            else:
                print(f'The popped element from the queue is {self.queue[self.front]}')
                self.queue[self.front]=None
                self.front+=1

    def peek(self):
        if self.front==len(self.queue):
            print('Nothing to display')
        else:
            print(f'The front element of the queue is: {self.queue[self.front]}')

    def display(self):
        if self.front==len(self.queue) and self.rear==len(self.queue):
            print('The queue is empty')
        else:
            for item in self.queue[self.front:self.rear]:
                print(f'|| {item}', end=' ')
            print()


if __name__ == '__main__':
    queueObject=Queue(int(input('Size of the queue: ')))

    while(True):
        print('1: Enqueue')
        print('2: Dequeue')
        print('3: Peek')
        print('4: Display')
        choice=int(input('Enter your choice: '))

        if choice==1:
            queueObject.enqueue()
        elif choice==2:
            queueObject.dequeue()
        elif choice==3:
            queueObject.peek()
        elif choice==4:
            queueObject.display()
        else:
            print('Error: Wrong Choice !!!')
