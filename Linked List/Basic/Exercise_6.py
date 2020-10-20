"""
Write a program to find the maximum and minimum element in the given linked list.
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

    def maxAndMin(self):
        maximum = self.head.data
        minimum = self.head.data
        iterator = self.head

        while iterator:

            if iterator.data >= maximum:
                maximum, iterator.data = iterator.data, maximum

            if iterator.data <= minimum:
                iterator.data, minimum = minimum, iterator.data

            iterator = iterator.next

        print(f'The maximum element of the linked list is: {maximum}')
        print(f'The minimum element of the linked list is: {minimum}')


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([12, 13, 64, 82, 2])
    ll.maxAndMin()
