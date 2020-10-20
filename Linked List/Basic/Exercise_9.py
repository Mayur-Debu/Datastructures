"""
Implementation of the circular doubly linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = self.tail = node
            self.head.next = self.head
            self.head.previous = None
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.tail.next = self.head

    def display(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            iterator = self.head
            print(iterator.data, end=' --> ')
            while iterator.next != self.head:
                iterator = iterator.next
                print(iterator.data, end=' --> ')
            print(None)


if __name__ == '__main__':
    cdll = CircularDoublyLinkedList()
    cdll.insertAtEnd(5)
    cdll.insertAtEnd(6)
    cdll.insertAtEnd(5)
    cdll.display()
