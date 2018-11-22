# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

# Idea: Dynamic Programming
#
# B[k;i] = max(B[k;i-1], S[k-1;i-1] - prices[i])
# S[k;i] = max(S[k;i-1], B[k;i-1] + prices[i])
#
# S[0;i] = 0
# S[k;0] = 0
# B[k;0] = -prices[0]
#
def max_profit_v1(K, prices):
    N = len(prices)
    S0, S1 = ([0] * (K+1) for _ in range(2))
    B0, B1 = ([0] * (K+1) for _ in range(2))
    for k in range(1, K+1):
        B0[k] = -prices[0]
    for i in range(1, N):
        for k in range(1, K+1):
            B1[k] = max(B0[k], S0[k-1] - prices[i])
            S1[k] = max(S0[k], B0[k] + prices[i])
        S0, S1 = S1, S0
        B0, B1 = B1, B0
    return S0[K]

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if k >= len(prices):
            return sum(max(0, a-b) for a, b in zip(prices[1:], prices[:-1]))
        return max_profit_v1(k, prices)
