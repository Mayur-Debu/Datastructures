"""
Implement a simple tree and add child to and print the simple tree data structure.
"""


class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self):
        spaces = '   ' * self.getLevel() * 3
        if self.parent:
            prefix = spaces + '|---'
        else:
            prefix = spaces
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def addChildren(self, child):
        child.parent = self
        self.children.append(child)


if __name__ == '__main__':
    root = Treenode("Electronics")

    mobile = Treenode("Mobile")
    mobile.addChildren(Treenode("MOBILE BRAND"))
    mobile.addChildren(Treenode("MOBILE BRAND"))
    mobile.addChildren(Treenode("MOBILE BRAND"))

    tv = Treenode("Television")
    tv.addChildren(Treenode("TV BRAND"))
    tv.addChildren(Treenode("TV BRAND"))
    tv.addChildren(Treenode("TV BRAND"))

    fridge = Treenode("Fridge")
    fridge.addChildren(Treenode("Fridge Brands"))
    fridge.addChildren(Treenode("Fridge Brands"))
    fridge.addChildren(Treenode("Fridge Brands"))

    root.addChildren(mobile)
    root.addChildren(tv)
    root.addChildren(fridge)

    root.printTree()
