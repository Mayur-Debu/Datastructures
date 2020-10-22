"""
Write a program to find intersection of two sorted linked list.
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
        string = set()

        for data in data_list:
            string.add(data)
            self.insertAtEnd(data)
        return string

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

    def lengthOfLinkedList(self):
        '''This function return the length of the linked list.'''
        iterator = self.head
        if iterator is None:
            print('The linked list is empty')
        else:
            counter = 0
            while iterator:
                counter += 1
                iterator = iterator.next
            return counter


if __name__ == '__main__':
    ll = LinkedList()
    string1 = set()
    string2 = set()
    string1 = ll.insertList([1, 2, 4, 5, 6])
    ll.print()
    string2 = ll.insertList([1, 2, 3])
    ll.print()
    string3 = string1.intersection(string2)
    print([item for item in string3])
