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
        '''This is the constructor used to define a new node .'''
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        '''The linkded list constructor initializes the head.'''
        self.head = None

    def insertAtBeginning(self, data):
        '''This function inserts the new node at the beginning of the linked list.'''
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        '''This function inserts the new node at the end of the linked list.'''
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data, None)

    def insertAtIndex(self, index, data):
        '''This function inserts the new node at the user defined index.'''
        if index < 0 or index >= self.lengthOfLinkedList():
            print('Invalid index')
        elif index == 0:
            self.insertAtBeginning(data)
            return
        else:
            iterator = self.head
            count = 0
            while iterator:
                if count == index - 1:
                    node = Node(data, iterator.next)
                    iterator.next = node
                    break
                iterator = iterator.next
                count += 1

    def insertList(self, data_list):
        '''This function inserts the list of nodes in the linked list.'''
        self.head = None

        for data in data_list:
            self.insertAtEnd(data)

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

    def removeElementAt(self, index):
        '''This function remove element present at the user defined location.'''
        if index < 0 or index >= self.lengthOfLinkedList():
            print('Invalid index number.')
        elif index == 0:
            self.head = self.head.next
            return
        else:
            counter = 0
            iterator = self.head
            while iterator:
                if counter == index - 1:
                    iterator.next = iterator.next.next
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
    ll.insertList([1, 2, 3, 4, 5])
    ll.print()
    ll.insertAtIndex(3, 3)
    ll.print()
