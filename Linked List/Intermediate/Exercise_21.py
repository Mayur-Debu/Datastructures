"""
write a function to count the number of nodes in circular linked lists.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            node.next = self.head

    def display(self):
        counter = 1
        iterator = self.head
        if self.head.data is None:
            print(f'The circular linked list is empty')
            print(f'The Number of nodes in the circular linked list is: 0')
        else:
            print(iterator.data, end=' --> ')
            while iterator.next != self.head:
                counter += 1
                iterator = iterator.next
                print(iterator.data, end=' --> ')
            print(None)
            print(f'The number of the nodes in the circular linked list is: {counter}')


if __name__ == '__main__':
    ll = CircularLinkedList()
    ll.insertAtEnd(6)
    ll.insertAtEnd(5)
    # ll.insertAtEnd(5)
    # ll.insertAtEnd(7)
    ll.display()
