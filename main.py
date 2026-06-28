"""
Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]

Ref:
https://www.geeksforgeeks.org/dsa/best-time-to-buy-and-sell-stock/
https://takeuforward.org/data-structure/stock-buy-and-sell
"""


def maxProfit(prices):
    minSoFar = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if minSoFar > prices[i]:
            minSoFar = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - minSoFar)
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
