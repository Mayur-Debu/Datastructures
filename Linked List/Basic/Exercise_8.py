"""
Write a program to implement the doubly linked list and perform following operations.
    1: add Node
    2: Delete Node
    3: print
    4: length of the linked lists

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def insertAtEnd(self, data):
        node = Node(data)

        if self.head.data is None:
            self.head = self.tail = node
            self.head.next = None
            self.head.previous = None
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.tail.next = None

    def deleteElementAt(self, index):
        if index == 0:
            self.head = self.head.next
            return
        else:
            counter = 0
            iterator = self.head
            while iterator:
                if counter == index - 1:
                    iterator.next = iterator.next.next
                iterator = iterator.next
                counter += 1

    def lengthOfDoublyLinkedList(self):
        counter = 0
        iterator = self.head
        while iterator:
            counter += 1
            iterator = iterator.next
        print(f'Length of the Doubly Linked List is: {counter}')

    def display(self):
        if self.head.data is None:
            print('Empty Linked List')
        else:
            iterator = self.head
            while iterator:
                print(iterator.data, end=' --> ')
                iterator = iterator.next
            print(None)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insertAtEnd(1)
    dll.insertAtEnd(2)
    dll.insertAtEnd(3)
    dll.insertAtEnd(4)
    dll.insertAtEnd(5)
    dll.display()
    dll.deleteElementAt(2)
    dll.display()
    dll.lengthOfDoublyLinkedList()
