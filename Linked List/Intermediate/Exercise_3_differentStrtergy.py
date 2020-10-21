"""Write a program to reverse a linked list"""


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

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)

    def reverseLinkedList(self):
        iterator = self.head
        string = []
        while iterator:
            string.append(iterator.data)
            iterator = iterator.next
        self.head = None
        self.insertList(string[::-1])


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4, 5])
    ll.display()
    ll.reverseLinkedList()
    ll.display()
