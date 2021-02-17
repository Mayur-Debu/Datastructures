"""
Balanced Parenthesis problem.
"""
class Stack:
    def __init__(self,size):
        self.size=size
        self.top=-1
        self.arr=[None]*self.size

    def push(self,element):
        if self.top == len(self.arr)-1:
            print('Stack Full')
        else:
            self.top+=1
            self.arr[self.top]==element

    def pop(self):
        if self.top==-1:
            
