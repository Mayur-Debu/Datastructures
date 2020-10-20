"""
Write a program to provide the nth node from the linked list.
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

    def nthNode(self, index):
        count = 0
        iterator = self.head
        while iterator:
            if count == index:
                print(f'The element at index {index} is: {iterator.data}')
            count += 1
            iterator = iterator.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList(['hi', 'i', 'm', 'mayur'])
    ll.nthNode(3)
