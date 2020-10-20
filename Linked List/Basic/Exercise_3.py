"""
Create a method to delete any element from the linked list.
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            iterator.next = Node(data, None)

    def insertList(self, datalist):
        self.head = None
        for data in datalist:
            self.insertAtEnd(data)

    def lengthOfLinkedList(self):
        if self.head == None:
            print('Empty Linked List')
        else:
            count = 0
            iterator = self.head
            while iterator:
                iterator = iterator.next
                count += 1
        return count

    def removeElementAt(self, index):
        if index < 0 or index >= self.lengthOfLinkedList():
            print('Invalid index number')
        elif index == 0:
            self.head = self.head.next
        else:
            iterator = self.head
            counter = 0
            while iterator:
                if counter == index - 1:
                    iterator.next = iterator.next.next
                iterator = iterator.next
                counter += 1

    def print(self):
        if self.head is None:
            print('Empty Linked list')
        else:
            iterator = self.head
            while iterator:
                print(iterator.data, end=' --> ')
                iterator = iterator.next
            print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 3, 4, 5])
    ll.print()
    ll.removeElementAt(2)
    ll.print()
