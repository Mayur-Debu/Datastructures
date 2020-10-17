"""
Write a program to implement a max heap using array.
"""
import numpy as np

class Maxheap:
    def __init__(self,size):
        self.size=size
        self.heap=[None]*self.size
        self.front=0
        self.rear=0

    def enqueue(self):
        if self.rear==len(self.heap):
            print('The queue is full')
        else:
            self.heap[self.rear]=int(input('Enter the element: '))
            self.rear+=1

    def dequeue(self):
        if self.front==len(self.heap):
            print('The queue is empty')
        else:
            print(f'The popped element from the queue is {self.heap[self.front]}')
            self.heap[self.front]=None
            self.front+=1



    def display(self):
        pass


if __name__ == '__main__':
    maxHeapObject=Maxheap(int(input('Size of queue: ')))
    while True:
        print('1: Enqueue')
        print('2: Dequeue')
        print('3: Display')
        choice=int(input('Enter your choice: '))

        if choice==1:
            maxHeapObject.enqueue()
        elif choice==2:
            maxHeapObject.dequeue()
        elif choice==3:
            maxHeapObject.display()
        else:
            print('Error: Wrong Choice!!!')