"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            output = prices[1] - prices[0]
            return output if output > 0 else 0
        i = 0
        j = 1
        stockBuy = prices[i]
        stockSell = prices[j]
        counter = 0
        profit = 0
        while counter < len(prices)-2:
            if stockSell - stockBuy < 0:
                i = counter + 1
                j = i + 1
            else:
                if prices[j+1] > prices[j]:
                    j += 1
                else:
                    profit = profit + (stockSell - stockBuy)
                    i = counter + 1
                    j = i + 1

            stockSell = prices[j]
            stockBuy = prices[i]
            counter += 1
        if (stockSell - stockBuy) > 0:
            profit = profit + (stockSell - stockBuy)
        return profit