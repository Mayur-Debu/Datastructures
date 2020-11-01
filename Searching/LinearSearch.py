"""Implementing the linear search using the array"""

def linearSearch():
    listOfNumbers=list(map(int,input('Enter the list of Numbers').split(',')))
    searchNumber=int(input('Enter the Number you want to search: '))

    for number in listOfNumbers:
        if number==searchNumber:
            print(f'Number found in the list')
            break
    else:
        print('Number not found in the list')


if __name__ == '__main__':
    linearSearch()