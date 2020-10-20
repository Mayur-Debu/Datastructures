"""
Implementation of the circular linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
        if self.head.data is None:
            print('Empty linked list')
        else:
            iterator = self.head
            print(iterator.data, end=' --> ')
            while iterator.next != self.head:
                iterator = iterator.next
                print(iterator.data, end=' --> ')
            print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtEnd(5)
    ll.insertAtEnd(6)
    ll.display()
