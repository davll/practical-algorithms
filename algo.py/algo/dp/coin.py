# Coin Changing

#
# Case 1: How many ways to get the amount x
#
# f[x;k]: the number of ways that make up the amount x
#         with 1...k coin types
#
# f[x;k] = 1                          if x = 0 and k = 0
#        = f[x;k-1]                   if x < coin[k] and k > 0
#        = f[x;k-1] + f[x-coin[k];k]  if x >= coin[k] and k > 0
#        = 0                          otherwise
#

def num_ways(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, amount+1):
            dp[i] += dp[i-c]
    return dp[amount]

#
# Case 2: 
#
# f[x]: the minimum number of coins that make up the amount x
# coins: the set of coins
#
# f[x] = 0                  if i = 0
#      = 1                  if i in coins
#      = min { f[i-c] + 1 for c in coins if f[i-c] is defined }
#                           if i > c for some c in coins
#      = undefined          otherwise
#

def min_coins(amount, coins):
    # suppose coins is an increasing sequence
    dp = [-1 for _ in range(amount+1)]
    dp[0] = 0
    for c in filter(lambda x: x <= amount, coins):
        dp[c] = 1
    for i in range(1, amount+1):
        s = [dp[i-c] + 1 for c in coins if i-c >= 0 and dp[i-c] != -1]
        if s:
            dp[i] = min(s)
        else:
            dp[i] = -1
    return dp[amount]
