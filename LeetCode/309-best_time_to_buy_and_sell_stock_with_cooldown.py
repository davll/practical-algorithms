# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
#
# Hint: Dynamic Programming
# Hint: State Machine
#
# s0: initial state
# s1: bought state
# s2: sold state
#
# s0[i] = max(s0[i-1], s2[i-1])
# s1[i] = max(s1[i-1], s0[i-1] - prices[i])
# s2[i] = s1[i-1] + prices[i]
#
# s0[0] = 0
# s1[0] = -prices[i]
# s2[0] = 0
#

def max_profit(prices):
    n = len(prices)
    s0 = [-1] * n
    s1 = [-1] * n
    s2 = [-1] * n
    s0[0] = 0
    s1[0] = -prices[0]
    s2[0] = 0
    for i in range(1, n):
        s0[i] = max(s0[i-1], s2[i-1])
        s1[i] = max(s1[i-1], s0[i-1] - prices[i])
        s2[i] = s1[i-1] + prices[i]
    return max(s0[n-1], s2[n-1])

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return max_profit(prices)
