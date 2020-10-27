"""
Write a program to split the linked list into two halves.
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

    def insertList(self, datalist):
        counter = 0
        for data in datalist:
            counter += 1
            self.insertAtEnd(data)
        self.print(counter // 2)

    def print(self, counter):
        print(counter)
        iterator = self.head
        for i in range(counter + 1):
            print(iterator.data, end=' ')
            iterator = iterator.next
        print()
        while iterator:
            print(iterator.data, end=' ')
            iterator = iterator.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4, 5])
    # ll.print()
