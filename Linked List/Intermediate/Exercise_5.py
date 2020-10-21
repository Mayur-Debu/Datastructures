"""
Write a program to detect a loop in the  linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            iterator.next = node

    def insertList(self, dataList):
        for data in dataList:
            self.insertAtEnd(data)
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = self.head.next.next  # static looping done here

    def isLoop(self):
        slow = self.head
        fast = self.head.next
        while slow is not None and fast is not None and fast.next is not None:
            if slow == fast:
                return 1
            slow = slow.next
            fast = fast.next.next
        return -1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([1, 2, 3, 4])
    print(ll.isLoop())
