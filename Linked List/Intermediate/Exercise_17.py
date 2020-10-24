"""
Find the middle element of the linked list.
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
            node.next = None

    def insertList(self, dataList):
        counter = 0
        for data in dataList:
            self.insertAtEnd(data)
            counter += 1
        self.print(counter // 2)

    def print(self, counter):
        iterator = self.head
        index = 0
        while (iterator):
            if index == counter:
                print(f'The middle element of the linked lists is: {iterator.data}')
                break
            else:
                index += 1
                iterator = iterator.next


if __name__ == '__main__':
    ll = LinkedList()
    length = ll.insertList([1, 2, 3, 5])
