"""
Write a function to delete the linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        '''This function inserts the new node at the end of the linked list.'''
        if self.head is None:
            self.head = Node(data)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data)

    def insertList(self, data_list):
        '''This function inserts the list of nodes in the linked list.'''
        self.head = None

        for data in data_list:
            self.insertAtEnd(data)

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

    def deleteLinkList(self):
        iterator = self.head
        while iterator:
            self.head = None
            iterator = iterator.next
        print('Link List deleted')


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4])
    ll.print()
    ll.deleteLinkList()
    ll.print()
