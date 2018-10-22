# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def max_profit(prices):
    n = len(prices)
    peak, valley = prices[0], prices[0]
    result = 0
    for i in range(1, n):
        if peak <= prices[i]:
            peak = prices[i]
        else:
            result += peak - valley
            peak = valley = prices[i]
    result += peak - valley
    return result

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return max_profit(prices)
