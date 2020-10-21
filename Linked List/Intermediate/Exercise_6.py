"""
Write a program to count the length of loop.
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

    def lengthOfLoop(self, loop):
        counter = 1
        iterator = self.head
        while iterator:
            iterator = iterator.next
            counter += 1
            if counter == loop:
                break
            else:
                pass
        counter = 0
        while iterator:
            counter += 1
            iterator = iterator.next

        print(f'The length of the loop is {counter}')

    def insertList(self, dataList, loop):

        for data in dataList:
            self.insertAtEnd(data)

        self.lengthOfLoop(loop)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([25, 14, 19, 33, 10, 21, 39, 90, 58, 45], 4)
