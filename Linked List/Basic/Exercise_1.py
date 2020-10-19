"""
Create a singly linked list class(members -> values and next pointer), with the following method:
    1: Create new node
    2: Add node at beginning
    3: Add node at end
    4: Length
    5: Print
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head

        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data, None)

    def insertList(self, data_list):
        self.head = None

        for data in data_list:
            self.insertAtEnd(data)

    def lengthOfLinkedList(self):
        iterator = self.head
        if iterator is None:
            print('The linked list is empty')
        else:
            counter = 0
            while iterator:
                counter += 1
                iterator = iterator.next
            print(f'The length of the linked list is {counter}')

    def removeElementAt(self, index):
        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        iterator = self.head
        while iterator:
            if counter == index - 1:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            counter += 1

    def print(self):
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
    ll.insertAtEnd(5)
    ll.insertAtEnd(10)
    ll.insertList(['hi', 'i', 'M', 'Mayur'])
    ll.print()
    ll.lengthOfLinkedList()
    ll.removeElementAt(1)
    # ll.removeElementAt(20)
    ll.print()
