"""
Write a program to find the pair that sums to a given number in doubly linked list.
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

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None

    def insertList(self, dataList):
        for data in dataList:
            self.insertAtEnd(data)

    def findSum(self, sum):
        firstPointer = self.head
        secondPointer = self.tail
        while firstPointer != secondPointer:
            if firstPointer.data + secondPointer.data == sum:
                print(f'{firstPointer.data, secondPointer.data}', end=',')
                firstPointer = firstPointer.next

            elif firstPointer.data + secondPointer.data > sum:
                secondPointer = secondPointer.prev
            elif firstPointer.data + secondPointer.data < sum:
                firstPointer = firstPointer.prev

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' <--> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insertList(sorted([1, 2, 4, 6, 5, 8, 9]))
    ll.display()
    ll.findSum(7)
