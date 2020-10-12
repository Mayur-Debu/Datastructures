"""
Write a program to reverse a string using stack.
"""


class ReverseString:
    def __init__(self, string):
        self.string = string
        self.top = -1
        self.arr = [None] * len(string)

    def reverse(self):
        for chareceter in self.string:
            self.top += 1
            self.arr[self.top] = chareceter

        print('Reversed sting is: ',end='')
        while self.top != -1:
            print(self.arr[self.top], end='')
            self.top -= 1


if __name__ == '__main__':
    string = input('Enter a string: ')
    reverseStringObject = ReverseString(string)
    reverseStringObject.reverse()
