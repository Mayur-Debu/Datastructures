"""
Reverse a linked list in group of given sizes.
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
            iterative = self.head
            while iterative.next:
                iterative = iterative.next
            iterative.next = node
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

    def reverseInChunks(self, index):
        counter = 1
        iterator = self.head
        string1 = []
        string2 = []
        while iterator:
            if counter <= index:
                string1.append(iterator.data)
                iterator = iterator.next
                counter += 1
            else:
                while iterator:
                    string2.append(iterator.data)
                    self.insertAtFront(iterator.data)
                    iterator = iterator.next
        self.reverse(string2, string1)

    def reverse(self, datalist1, datalist2):
        self.head = None
        for data in datalist1:
            self.insertAtFront(data)
        for data in datalist2:
            self.insertAtFront(data)

    def print(self):
        '''This function prints the linked list starting from the head till the tail.'''
        if self.head is None:
            print('The linked list is empty')
            return

        iterator = self.head

        while iterator:
            print(iterator.data, end=' -->')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 2, 4, 5, 6, 7, 8])
    ll.print()
    ll.reverseInChunks(4)
    ll.print()
