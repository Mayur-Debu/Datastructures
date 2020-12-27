"""Implement linear search using linked list."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            node.next = None
        else:
            iterator = self.head
            while iterator.next != None:
                iterator = iterator.next
            iterator.next = node
            node.next = None

    def linearSearch(self):
        dataList = list(
            map(int, input('Enter the list of elements, separating the individual elements with a \',\': ').split(',')))
        for data in dataList:
            self.insertAtEnd(data)
        searchElement = int(input('Enter the number to be searched: '))
        for element in dataList:
            if element == searchElement:
                return True
        return False

    def displayData(self):
        if self.head is None:
            print('Empty Linked List')
        else:
            iterator = self.head
            while iterator:
                print(f'{iterator.data}', end='--> ')
                iterator = iterator.next
            print(None)


if __name__ == '__main__':
    ll = LinkedList()
    print(ll.linearSearch())
