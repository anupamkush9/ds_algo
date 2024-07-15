# Python program for the above approach:


def maxProfit(prices, n):
    buy = prices[0]
    max_profit = 0
    for i in range(1, n):

        # Checking for lower buy value
        if (buy > prices[i]):
            buy = prices[i]

        # Checking for higher profit
        elif (prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit


# Driver code
if __name__ == '__main__':

    prices = [7, 1, 5, 6, 4]
    n = len(prices)
    max_profit = maxProfit(prices, n)
    print(max_profit)

# ref: 
# https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/
# best time to buy stock
