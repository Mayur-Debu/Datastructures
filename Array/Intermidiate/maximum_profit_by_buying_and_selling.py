'''
Maximum profit by buying and selling a share at most twice
'''


def minima(prices, pointer):
    if (prices[pointer] < prices[pointer + 1]):
        return prices[pointer]
    else:
        pointer += 1
        minima(prices, pointer)


def maxima(prices, pointer):
    if (prices[pointer] > prices[pointer + 1]):
        return prices[pointer]
    else:
        pointer += 1
        maxima(prices, pointer)


def maximize_profit(prices, n):
    local_maxima = []
    local_minima = []
    pointer = 0
    for i in range(len(prices)):
        local_minima.append(minima(prices,pointer))


    print(local_minima)
    print(local_maxima)


if __name__ == '__main__':
    prices = []
    prices = list(map(int, input('Enter the prices of stock: ').strip(" ").split(" ")))
    maximize_profit(prices, len(prices))
