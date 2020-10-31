"""
Rotate a Doubly Linked List by N nodes.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
            self.head.next = self.tail

        else:
            self.tail.next = node
            self.tail = node

    def insertList(self, dataList):
        for data in dataList:
            self.insertAtEnd(data)

    def rotateLinkedList(self, n):
        count = 0
        while count < n:
            count += 1
            self.tail.next = self.head
            self.tail = self.head
            self.head = self.head.next
            self.tail.next = None

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' <--> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insertList([1, 2, 3, 4])
    ll.display()
    ll.rotateLinkedList(2)
    ll.display()
