"""
Write a program to check the expression if it has a balanced/valid parenthesis or not.
"""


class BalancedParenthesis:

    def __init__(self, string):
        self.string = string
        self.arr = [None] * len(string)
        self.top = -1

    def checkValidity(self):

        for parenthesis in self.string:

            # condition for opening bracket

            if parenthesis == '{' or parenthesis == '[' or parenthesis == '(':
                self.top += 1
                self.arr[self.top] = parenthesis

            # condition for closing bracket
            elif parenthesis == '}':
                if self.arr[self.top] == '{':
                    self.arr[self.top] = None
                    self.top -= 1
            elif parenthesis == ']':
                if self.arr[self.top] == '[':
                    self.arr[self.top] = None
                    self.top -= 1
            elif parenthesis == ')':
                if self.arr[self.top] == '(':
                    self.arr[self.top] = None
                    self.top -= 1

            else:
                print('Error: Invalid Expression!!!')
                break

        # Check for empty stack.
        # Empty stack denotes valid parenthesis.
        if self.top == -1:
            print('Valid Expression')
        else:
            print('Error: Invalid Expression!!!')


if __name__ == '__main__':
    string = input('Enter a string: ')
    balancedParenthesisObject = BalancedParenthesis(string)
    balancedParenthesisObject.checkValidity()
