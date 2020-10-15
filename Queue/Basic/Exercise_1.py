"""
Implement the queue using array with the following operations:
    1:Enqueue
    2:Dequeue
    3:Front
    4:Display
"""

class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.rear=len(self.queue)
        self.front=len(self.queue)-1

    def enqueue(self):
        if self.rear==-1:
            print('The queue\'s overloaded.')
        else:
            self.rear-=1
            self.queue[self.rear]=int(input('Enter element in the queue: '))

    def dequeue(self):
        if self.front==-1:
            print('The queue\'s underflow.')
        else:
            print(f'The dequeued element from the queue is {self.queue[self.front]}')
            self.front-=1

    def peek(self):
        if self.front==-1:
            print('The queue\'s empty nothing to display.')
        else:
            print(f'The peek element of the queue is {self.front}')

    def display(self):
        if self.front==-1 and self.rear==-1:
            print('The queue\'s empty.')
        else:
            for item in self.queue[self.front:self.rear]:
                print(f'{item} ||',end='')
            print()



if __name__ == '__main__':
    queueObject=Queue(int(input('Enter the size of queue: ')))
<<<<<<< HEAD

    while(True):
        print('1:Enqueue')
        print('2:Dequeue')
        print('3:Peek')
        print('4:Display')
        choice = int(input('Enter your choice: '))
=======
    print('1:Enqueue')
    print('2:Dequeue')
    print('3:Peek')
    print('4:Display')
    choice=int(input('Enter your choice: '))

    while(True):

        if choice==1:
            queueObject.enqueue()
        elif choice==2:
            queueObject.dequeue()
        elif choice==3:
            queueObject.peek()
        elif choice==4:
            queueObject.display()
        else:
            print('Error: Wrong choice, Please try again!!!')

