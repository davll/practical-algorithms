# Coin Change Problem
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

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        for c in coins:
            if c == amount:
                return 1
        dp = [-1 for _ in range(amount+1)]
        # amount = 0 needs 0 coins
        dp[0] = 0
        # amount = c needs 1 coin
        for c in filter(lambda x: x <= amount, coins):
            dp[c] = 1
        # dynamic programming
        for i in range(1, amount+1):
            s = [dp[i-c] + 1 for c in coins if i-c >= 0 and dp[i-c] != -1]
            if s:
                dp[i] = min(s)
            else:
                dp[i] = -1
        return dp[amount]
