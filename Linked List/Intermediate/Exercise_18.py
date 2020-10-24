"""
Write a program to check if a given linked list is circular.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

    def display(self):
        iterator = self.head
        while iterator:
            if iterator.next == self.head:
                print('1')
                break
            iterator = iterator.next
        else:
            print('0')


if __name__ == '__main__':
    ll = CircularLinkedList()
    ll.insertAtEnd(5)
    ll.insertAtEnd(6)
    ll.display()
