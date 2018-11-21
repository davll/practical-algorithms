# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Hint: Dynamic Programming
#
# s0: idle state
# s1: bought state
#
# s0[i] = max(s0[i-1], s1[i-1] + prices[i] - fee)
# s1[i] = max(s1[i-1], s0[i-1] - prices[i])
#
# s0[0] = 0
# s1[0] = -prices[0]
#
def max_profit_v1(prices, fee):
    n = len(prices)
    s0, s1 = [0] * n, [0] * n
    s1[0] = -prices[0]
    for i in range(1, n):
        s0[i] = max(s0[i-1], s1[i-1] + prices[i] - fee)
        s1[i] = max(s1[i-1], s0[i-1] - prices[i])
    return s0[-1]

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        return max_profit_v1(prices, fee)
