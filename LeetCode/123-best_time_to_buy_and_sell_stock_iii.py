# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity

# Idea: Dynamic Programming
#
# s0: start
# b1: first bought
# s1: first sold
# b2: second bought
# s2: second sold
#
# s0[i] = s0[i-1]
# b1[i] = max(b1[i-1], s0[i-1] - prices[i])
# s1[i] = max(s1[i-1], b1[i-1] + prices[i])
# b2[i] = max(b2[i-1], s1[i-1] - prices[i])
# s2[i] = max(s2[i-1], b2[i-1] + prices[i])
#
# s0[0] = 0
# b1[0] = -prices[0]
# s1[0] = 0
# b2[0] = -prices[0]
# s2[0] = 0
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

# Idea: Dynamic Programming
#
# F[k;i] = max {
#              # do nothing
#              F[k;i-1]
#
#              # buy on day 0, sell on day i
#              prices[i] - prices[0]
#
#              # buy on day j, sell on day i
#              prices[i] - prices[j] + F[k-1;j-1] for 1 <= j < i
#
#              # btw, j can be i as well => miss the k-th transaction
#          }
#
def max_profit_v2(prices):
    N = len(prices)
    K = 2
    F = [[0] * N for _ in range(K+1)]
    # profit = 0 when k = 0
    for k in range(1, K+1):
        for i in range(1, N):
            # buy on day 0, sell on day i
            minval = prices[0]
            for j in range(1, i):
                # buy on day j, sell on day i
                minval = min(minval, prices[j] - F[k-1][j-1])
            # sell on day i or not
            F[k][i] = max(F[k][i-1], prices[i] - minval)
    return F[K][-1]

# Improved over v2
#
# repeated computation on minval can be eliminated
#
def max_profit_v3(prices):
    N = len(prices)
    K = 2
    F = [[0] * N for _ in range(K+1)]
    for k in range(1, K+1):
        minval = prices[0]
        for i in range(1, N):
            F[k][i] = max(F[k][i-1], prices[i] - minval)
            minval = min(minval, prices[i] - F[k-1][i-1])
    return F[K][-1]

# Swap the two for-loops
def max_profit_v4(prices):
    N = len(prices)
    K = 2
    F = [[0] * N for _ in range(K+1)]
    M = [prices[0]] * (K+1)
    for i in range(1, N):
        for k in range(1, K+1):
            F[k][i] = max(F[k][i-1], prices[i] - M[k])
            M[k] = min(M[k], prices[i] - F[k-1][i-1])
    return F[K][-1]

# optimize space
def max_profit_v5(prices):
    N = len(prices)
    K = 2
    F = [0] * (K+1)
    M = [prices[0]] * (K+1)
    for i in range(1, N):
        for k in range(1, K+1):
            F[k] = max(F[k], prices[i] - M[k])
            M[k] = min(M[k], prices[i] - F[k-1])
    return F[K]

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return max_profit_v5(prices)
