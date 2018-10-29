class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
