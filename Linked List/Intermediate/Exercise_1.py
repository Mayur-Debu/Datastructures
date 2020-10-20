"""
Write a program to get the nth node from the end of the singly linked list.
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

    def lengthOfLinkedList(self):
        iterator = self.head
        counter = 0
        while iterator:
            iterator = iterator.next
            counter += 1
        return counter

    def nthNodeFromTheEnd(self, index):
        if index < 0 or index > self.lengthOfLinkedList():
            print('Invalid index number')

        iterator_value = self.lengthOfLinkedList() - index
        iterator = self.head
        counter = 0
        while iterator:
            if counter == iterator_value:
                print(f'The {index}nt node from the end is: {iterator.data}')
                return
            iterator = iterator.next
            counter += 1

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
    ll.insertList([1, 2, 3, 4, 5, 6])
    ll.print()
    ll.nthNodeFromTheEnd(5)
