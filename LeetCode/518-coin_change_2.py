# Coin Change Problem
#
# f[x;k]: the number of ways that make up the amount x
#         with 1...k coin types
#
# f[x;k] = 1                          if x = 0 and k = 0
#        = f[x;k-1]                   if x < coin[k] and k > 0
#        = f[x;k-1] + f[x-coin[k];k]  if x >= coin[k] and k > 0
#        = 0                          otherwise
#

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
        return dp[amount]

if __name__ == "__main__":
    s = Solution()
    amount = int(input("amount? "))
    n = int(input("num of coins? "))
    coins = [int(input("coin[" + str(i) + "]? ")) for i in range(n)]
    ans = s.change(amount, coins)
    print("ans = " + str(ans))
