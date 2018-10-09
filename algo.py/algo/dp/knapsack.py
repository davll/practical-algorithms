# 0/1 Knapsack Problem
#
# Given weights and values of n items, put these items in a knapsack of
# capacity W to get the maximum total value in the knapsack.
#
# f[c,n]: maximum value of n items that can be put in a knapsack of capacity c
#
# f[c,n] = 0                    if n = 0 or c = 0
#        = f[c,n-1]             if weights[n-1] > capacity
#        = max {
#              f[c-w, n-1] + v,
#              f[c, n-1]
#          }                    otherwise
#          where w = weights[n-1], v = values[n-1]
#

def knapsack(capacity, weights, values, n):
    assert len(weights) == n
    assert len(values) == n
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w, v = weights[i-1], values[i-1]
        for c in range(1,capacity+1):
            if w > c:
                dp[i][c] = dp[i-1][c]
            else:
                dp[i][c] = max(dp[i-1][c], dp[i-1][c-w] + v)
    return dp[n][capacity]
