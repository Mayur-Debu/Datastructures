"""
Write a program to add two numbers represented by a linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            node.next = self.head
            self.head = node

    def insertAtEnd(self):
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(0)

    def insertList(self, datalist):
        length = len(datalist)
        for data in datalist:
            self.insertAtFront(data)
        return length

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll1 = LinkedList()
    ll2 = LinkedList()
    length1 = ll1.insertList([9, 9, 9, 9])
    length2 = ll2.insertList([9, 9, 9, 9])

    if length1 == length2:
        pass
    else:
        if length1 > length2:
            for i in range(length1 - length2):
                ll2.insertAtEnd()
            length2 = length1
        else:
            for i in range(length2 - length1):
                ll1.insertAtEnd()
            length1 = length2

    ll1.display()
    ll2.display()
    print(length1, length2)

    carry = 0
    iterator1 = ll1.head
    iterator2 = ll2.head

    for _ in range(length1 and length2):
        ans = iterator1.data + iterator2.data + carry

        if ans == 10 and iterator1.next is not None and iterator2.next is not None:
            carry = 1
            ans = 0
            print(ans, end=' ')
        elif ans > 10 and iterator1.next is not None and iterator2.next is not None:
            carry = 1
            ans = ans - 10
            print(ans, end=' ')
        else:
            print(ans, end=' ')
            carry = 0
        iterator1 = iterator1.next
        iterator2 = iterator2.next
