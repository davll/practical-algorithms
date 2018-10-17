# similar to coin change problem

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        coins = list(range(2, n))
        dp = [0] * (n+1)
        dp[0:3] = [1,1,1]
        for i in range(3, n+1):
            for c in filter(lambda x: x < i, coins):
                x1 = c * dp[i-c]
                x2 = c * (i-c)
                x3 = dp[c] * dp[i-c]
                x4 = dp[c] * (i-c)
                dp[i] = max(dp[i], x1, x2, x3, x4)
        return dp[n]
