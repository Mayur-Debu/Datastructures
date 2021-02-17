"""
Implement the tree in given structure:

Nipul (CEO)
    |---Chinmay (CTO)
        |---Vishwa (Infrastructure Head)
            |---Dhaval(Cloud manager)
            |---Abhijit(App Manager)
        |---Aamir (Application Head)
    |---Gels (HR Head)
"""


class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChildren(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + " |---"
        if self.parent:
            print(prefix + self.data)
        else:
            print(self.data)

        if self.children:
            for child in self.children:
                child.printTree()


if __name__ == '__main__':
    root = Treenode("Nipul (CEO)")

    CTO = Treenode("Chinmay (CTO)")
    vishwa = Treenode("Vishwa (Infrastructure Head")
    CTO.addChildren(vishwa)
    CTO.addChildren(Treenode("Aamir (Application Head)"))

    vishwa.addChildren(Treenode("Dhaval (Cloud Manager)"))
    vishwa.addChildren(Treenode('Abhijit (App Manager)'))

    HR = Treenode("Gels (HR HEAD)")

    root.addChildren(CTO)
    root.addChildren(HR)

    root.printTree()
