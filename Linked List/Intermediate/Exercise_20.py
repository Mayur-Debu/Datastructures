"""
Function for deletion from a linked list.
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
            self.tail.next = self.head

    def deleteElement(self, element):
        iterator = self.head
        while iterator:
            # Condition for deleting first element
            if iterator.data == element:
                print(f'deleted element is: {iterator.data}')
                self.head = iterator.next
                self.tail.next = self.head
                break
            # Condition for deleting last element
            elif iterator.next.data == element and iterator.next == self.tail:
                print(f'the deleted element is {iterator.next.data}')
                self.tail = iterator
                self.tail.next = self.head
                break
            # condition for deleting other element
            else:
                if iterator.next.data == element:
                    print(f'the deleted element is {iterator.next.data}')
                    iterator.next = iterator.next.next
                    break
            iterator = iterator.next

    def display(self):
        if self.head.data is None:
            print('Empty linked list')
        else:
            iterator = self.head
            print(iterator.data, end=' --> ')
            while iterator.next != self.head:
                iterator = iterator.next
                print(iterator.data, end=' --> ')
            print(None)


if __name__ == '__main__':
    ll = CircularLinkedList()
    ll.insertAtEnd(5)
    ll.insertAtEnd(6)
    ll.insertAtEnd(7)
    ll.insertAtEnd(8)

    ll.display()

    ll.deleteElement(6)
    ll.display()
