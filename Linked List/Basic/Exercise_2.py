"""
Create a function to search a element in the linked list.
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
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

    def search(self, searchNumber):
        '''This function searches for data in the linked list and return the index number of the searched item.'''
        if self.head == None:
            print('Empty Linked List')
        else:
            iterator = self.head
            count = 0
            while iterator:
                if iterator.data == searchNumber:
                    print(f'The searched element is at index: {count}')
                    break
                else:
                    count += 1
                    iterator = iterator.next
            else:
                print('Searched number not in linked list')

    def print(self):

        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4, 5])
    ll.print()
    ll.search(1)
