"""
Write a program to reverse a doubly linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.previous = None
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            node.next = None

    def insertList(self, datalist):
        for data in datalist:
            self.insertAtEnd(data)

    def reverse(self):
        self.head = Node(None)
        iterator = self.tail
        while iterator:
            self.insertAtEnd(iterator.data)
            iterator = iterator.previous

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insertList([1, 2, 3])
    ll.display()
    ll.reverse()
    ll.display()
