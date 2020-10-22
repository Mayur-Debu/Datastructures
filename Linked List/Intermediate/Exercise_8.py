"""
Write a program to remove duplicates from the sorted linked list.
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
        string = []
        for data in data_list:
            string.append(data)
            self.insertAtEnd(data)
        print('Original Linked list:', end=' ')
        self.print()
        print('Altered Linked list:', end=' ')
        self.removeDuplicates(sorted(set(string)))

    def removeDuplicates(self, string):
        self.head = None
        for data in string:
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


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList(['a','b','b','v'])
    ll.print()
