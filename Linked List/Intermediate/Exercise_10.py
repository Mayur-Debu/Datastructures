"""
Write a program to move the last element ot the front of the linked list.
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

    def insertAtFront(self, data):
        node = Node(data)
        self.head = node

    def lastToFront(self, dataList):
        initial = dataList[-1]
        dataList.__delitem__(-1)

        self.insertAtFront(initial)
        for data in dataList:
            self.insertAtEnd(data)

    def print(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.lastToFront(list(map(int, input('Enter the element in list: ').strip(' ').split(' '))))
    ll.print()
