"""
Write a program to count the number of triplets in DLL.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insertList(self, datalist):
        for data in datalist:
            self.insertAtEnd(data)

    def noOfTriplets(self, sum):
        count = 0
        iterator = self.head
        firstPointer = iterator.next
        secondPointer = self.tail
        set_of_number = set()

        while iterator is not None and firstPointer is not None and secondPointer is not None:
            while firstPointer is not None:
                if iterator.data + firstPointer.data + secondPointer.data == sum:

                    print(iterator.data, firstPointer.data, secondPointer.data)
                    count += 1
                    secondPointer = secondPointer.prev
                else:
                    firstPointer = firstPointer.next

            iterator = iterator.next
            secondPointer = secondPointer.prev

        return count

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4, 5, 6])
    ll.display()
    print(ll.noOfTriplets(12))
