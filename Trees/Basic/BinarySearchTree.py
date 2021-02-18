"""
Implement the binary search tree.
"""


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChildren(self, child):
        if child == self.data:
            return

        if child < self.data:
            if self.left:
                self.left.addChildren(child)
            else:
                self.left = BinarySearchTree(child)
        else:
            if self.right:
                self.right.addChildren(child)
            else:
                self.right = BinarySearchTree(child)

    def search(self, val):
        if self.data == val:
            return True
        elif self.data == '':
            return False

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()

        if self.data == '':
            pass
        else:
            elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def postOrderTraversal(self):
        elements=[]
        if self.left:
            elements+= self.left.postOrderTraversal()

        if self.right:
            elements+=self.right.postOrderTraversal()

        if self.data == '':
            pass
        else:
            elements.append(self.data)

        return elements

    def preOrderTraversal(self):
        elements=[]
        if self.data=='':
            pass
        else:
            elements.append(self.data)

        if self.left:
            elements+=self.left.preOrderTraversal()
        if self.right:
            elements+=self.right.preOrderTraversal()

        return elements


    def deleteNode(self, data):
        if data == self.data:
            self.data = ''
            print(f'Deleted {data}')
            return ''

        if data < self.data:
            if self.left:
                return self.left.deleteNode(data)

        if data > self.data:
            if self.right:
                return self.right.deleteNode(data)

    def getMax(self):
        elements = []
        elements = self.inOrderTraversal()
        return max(elements)

    def getMin(self):
        elements = []
        elements = self.inOrderTraversal()
        return min(elements)


if __name__ == '__main__':
    elements = [5, 12, 4, 3, 2, 1]
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.addChildren(elements[i])

    print(f'Inorder Traversal: {root.inOrderTraversal()}')  # Get the inorder Traversal
    print(f'Postorder Traversal: {root.postOrderTraversal()}')  #Get the postorder traversal
    print(f'Preorder Traversal: {root.preOrderTraversal()}')    #get the preorder traversal

    # root.deleteNode(3)  # Delete the given node
    # print(root.inOrderTraversal())

    print(root.search(3))  # Search for the element

    print(root.getMax())    #Get Maximum element
    print(root.getMin())    #Get Minimum element

