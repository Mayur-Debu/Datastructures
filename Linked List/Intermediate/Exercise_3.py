"""
Write  a program to reverse a linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            iterator.next = node
            node.next = None

    def insertList(self, dataList):
        for data in dataList:
            self.insertAtEnd(data)

    def insertAtFront(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            node.next = self.head
            self.head = node

    def reverseIterative(self):
        iterative = self.head
        self.head = None
        while iterative:
            self.insertAtFront(iterative.data)
            iterative = iterative.next

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4])
    ll.display()
    ll.reverseIterative()
    ll.display()
