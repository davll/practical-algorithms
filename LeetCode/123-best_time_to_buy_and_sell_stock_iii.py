# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity

# Idea: Dynamic Programming
#
# s0: start
# s1: first bought
# s2: first sold
# s3: second bought
# s4: second sold
#
# s0[i] = s0[i-1]
# s1[i] = max(s1[i-1], s0[i-1] - prices[i])
# s2[i] = max(s2[i-1], s1[i-1] + prices[i])
# s3[i] = max(s3[i-1], s2[i-1] - prices[i])
# s4[i] = max(s4[i-1], s3[i-1] + prices[i])
#
# s0[0] = 0
# s1[0] = -prices[0]
# s2[0] = 0
# s3[0] = -prices[0]
# s4[0] = 0
#
def max_profit_v1(prices):
    n = len(prices)
    s0, s1, s2, s3, s4 = ([0] * n for _ in range(5))
    s1[0] = -prices[0]
    s3[0] = -prices[0]
    for i in range(1, n):
        s0[i] = s0[i-1]
        s1[i] = max(s1[i-1], s0[i-1] - prices[i])
        s2[i] = max(s2[i-1], s1[i-1] + prices[i])
        s3[i] = max(s3[i-1], s2[i-1] - prices[i])
        s4[i] = max(s4[i-1], s3[i-1] + prices[i])
    return s4[-1]

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return max_profit_v1(prices)
