'''
Implement K stack in a single array
'''
class Twostack:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=self.size

    def push1(self,x):

        if(self.top1<self.top2-1):
            self.top1+=1
            self.arr[self.top1]=x
            print(self.arr)
        else:
            print('Stack Overflow')

    def push2(self,x):

        if(self.top1<self.top2-1):
            self.top2-=1
            self.arr[self.top2]=x
            print(self.arr)
        else:
            print('Stack Overflow')

    def pop1(self):
        if(self.top1>=0):
            print(f'The popped element is: {self.arr[self.top1]} ')
            self.arr[self.top1]=None
            self.top1-=1
            print(self.arr)
        else:
            print('Stack Underflow')


    def pop2(self):
        if(self.top2<self.size):
            print(f'The popped element is: {self.arr[self.top2]} ')
            self.arr[self.top2]=None
            self.top2+=1
            print(self.arr)
        else:
            print('Stack Underflow')




if __name__ == '__main__':
    stackObject=Twostack(5)
    stackObject.push1(5)
    stackObject.pop1()
    stackObject.push2(15)
    stackObject.push2(15)
    stackObject.push2(15)
    stackObject.push2(15)
    stackObject.push2(15)
    stackObject.push1(12)
    stackObject.pop2()
    stackObject.push1(12)
