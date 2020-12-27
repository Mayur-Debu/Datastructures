""" Implement binary search using linked list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            iterator = self.head
            while iterator.next != None:
                iterator = iterator.next
            self.tail = node
            node.next = None

    def insertList(self):
        dataList = list(map(int, input('Enter the element sin linked list: ').split(',')))
        dataList = sorted(dataList)
        for data in dataList:
            self.insertAtEnd(data)
        # searchNumber=int(input('Enter the number to be searched: '))
        #
        # low=self.head
        # high=self.tail

    def display(self):
        iterator = self.head
        while iterator.next != None:
            print(f'{iterator.data}', end=' --> ')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList()
    ll.display()
