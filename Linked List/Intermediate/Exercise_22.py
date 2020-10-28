"""
Write a program to swap the head and tail node of a linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertList(self, dataList):
        for data in dataList:
            self.insertAtEnd(data)

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)

    def swap(self):
        self.head.data, self.tail.data = self.tail.data, self.head.data
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4])
    ll.display()
    ll.swap()
