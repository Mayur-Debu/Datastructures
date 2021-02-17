class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertElement(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            iterator=self.head
            while iterator.next:
                iterator=iterator.next
            iterator.next=node

    def insertListOfElement(self,arr):
        self.head=None
        for elements in arr:
            self.insertElement(elements)

    def printList(self):
        iterator=self.head
        while iterator.next:
            print(iterator.data,end=' --> ')
            iterator=iterator.next
        print('None')


if __name__ == '__main__':
    ll=LinkedList()
    arr=[1,2,3,4,5]
    ll.insertListOfElement(arr)
    ll.printList()
