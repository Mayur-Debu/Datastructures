"""
Write a program to check whether the singly linked list is a palindrome or not.
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

    def checkPalindrome(self):
        string = []
        iterator = self.head
        while iterator:
            string.append(iterator.data)
            iterator = iterator.next

        if string == string[::-1]:
            print(1)
        else:
            print(-1)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4])
    ll.checkPalindrome()
