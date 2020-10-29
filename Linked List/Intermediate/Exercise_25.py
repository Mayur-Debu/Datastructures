"""
Write a program to count the number of triplets in DLL.
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
        counter=0
        iterator=self.head
        firstPointer=iterator.next
        while iterator.next!=self.tail:
            if iterator.data+iterator.next.data+self.tail.data==sum:
                counter+=1
                break
            else:
                firstPointer=firstPointer.next

        print(counter)


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
    ll.findSum(17)
