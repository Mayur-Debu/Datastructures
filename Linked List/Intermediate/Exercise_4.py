"""
Reverse a linked list in group of given sizes.
"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertAtEnd(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
            node.next=None

    def insertList(self,datalist):
        for data in datalist:
            self.insertAtEnd(data)

    def reverseInGroup(self,n):
        iterator=self.head
        string=[]
        counter=0
        while iterator:
            if counter<n:
                string.append(iterator.data)
                counter+=1
            else:
                for data in string:
                    self.head=None
                    self.insertAtEnd(data)

    def display(self):
        iterator=self.head
        while iterator:
            print(iterator.data,end=' --> ')
            iterator=iterator.next
        print(None)

if __name__ == '__main__':
    ll=LinkedList()
    ll.insertList([1,2,3,4])
    ll.display()
    ll.reverseInGroup(2)
    ll.display()