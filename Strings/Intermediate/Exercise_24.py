""" Find the first repeated word in the string."""


def firstRepeatedWord(string):
    for i in range(len(string)):
        if string[i] in string[i + 1:]:
            return f'First repeating word is {string[i]}'
    else:
        return '-1'


if __name__ == '__main__':
    string = list(map(str, input('Enter the string: ').split(" ")))
    print(string)
    print(firstRepeatedWord(string))


