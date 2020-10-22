"""
Write a program to add 1 to a number represented as linked list.
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

    def add1(self, string):
        for item in range(len(string)):
            if item == len(string) - 1:
                print(string[item] + 1)
            else:
                print(string[item], end=' ')

    def insertList(self, data_list):
        '''This function inserts the list of nodes in the linked list.'''
        self.head = None
        string = []

        for data in data_list:
            string.append(data)
            self.insertAtEnd(data)

        self.add1(string)

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
    ll.insertList([4, 5, 6])
