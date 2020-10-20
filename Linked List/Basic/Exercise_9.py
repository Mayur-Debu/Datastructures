"""
Implementation of the circular doubly linked list.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            node.next=node
            node.previous=node
        else:
            iterator=self.head
            while iterator.next:
                iterator=iterator.next
            iterator.next=node
            node.next=self.head
            node.previous=iterator

    def display(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            iterator=self.head
            print(iterator.data,end=' --> ')
            iterator=iterator.next
            while iterator.next!=self.head:
                print(iterator.data,end=' --> ')
                iterator=iterator.next
            print(None)

if __name__ == '__main__':
    cdll=CircularDoublyLinkedList()
    cdll.insertAtEnd(5)
    cdll.insertAtEnd(6)
    # cdll.insertAtEnd(5)
    cdll.display()