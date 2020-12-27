""" Implement binary search using linked list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertElement(self, data):
        node = Node(data)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            node.next = None

    def insertList(self, dataList):
        dataList=sorted(dataList)
        length=len(dataList)
        for data in dataList:
            self.insertElement(data)
        SearchElement=int(input('Enter the Number to be searched: '))
        high=length
        low=1

        while low<high:
            mid=(high+low)//2



    def displayLinkedList(self):
        iterator = self.head
        while iterator:
            print(f'{iterator.data}', end='-->')
            iterator = iterator.next
        print(None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertList([12, 3, 4])
    ll.displayLinkedList()

