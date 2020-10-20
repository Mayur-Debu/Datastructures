"""
Create a function that counts the specific number of value in the linked list.
"""


class Node:
    def __init__(self, data=None, next=None):
        '''This is the constructor used to define a new node .'''
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        '''The linkded list constructor initializes the head.'''
        self.head = None

    def insertAtEnd(self, data):
        '''This function inserts the new node at the end of the linked list.'''
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data, None)

    def insertList(self, data_list):
        '''This function inserts the list of nodes in the linked list.'''
        self.head = None

        for data in data_list:
            self.insertAtEnd(data)

    def count(self, info):
        iterator = self.head
        count = 0
        while iterator:
            if iterator.data == info:
                count += 1
            iterator = iterator.next
        print(f'The given data appears {count} times in the given linked list')


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 2, 2, 2, 2, 3, 3, 4])
    ll.count(3)
