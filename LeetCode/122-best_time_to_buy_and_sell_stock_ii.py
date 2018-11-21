# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Idea: Dynamic Programming
#
# s0: idle state
# s1: bought state
#
# s0[i] = max(s0[i-1], s1[i-1] + prices[i])
# s1[i] = max(s1[i-1], s0[i-1] - prices[i])
#
# s0[0] = 0
# s1[0] = -prices[0]
#
def max_profit_v1(prices):
    n = len(prices)
    s0, s1 = [0] * n, [0] * n
    s1[0] = -prices[0]
    for i in range(1, n):
        s0[i] = max(s0[i-1], s1[i-1] + prices[i])
        s1[i] = max(s1[i-1], s0[i-1] - prices[i])
    return s0[-1]

# Idea: Greedy Method
def max_profit_v2(prices):
    n = len(prices)
    peak, valley = prices[0], prices[0]
    result = 0
    for i in range(1, n):
        if peak <= prices[i]:
            # ascending
            peak = prices[i]
        else:
            # declining
            result += peak - valley
            peak = valley = prices[i]
    result += peak - valley
    return result

# Idea: Greedy Method
def max_profit_v3(prices):
    n = len(prices)
    result = 0
    for i in range(1, n):
        if prices[i-1] < prices[i]:
            result += prices[i] - prices[i-1]
    return result

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return max_profit_v3(prices)
