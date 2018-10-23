# Integer Break
#
# Given a positive integer n, break it into the sum of at least
# two positive integers and maximize the product of those integers.
# Return the maximum product you can get.
#
# Solution 1:
#
# similar to coin change problem
#
# f[n] = the maximum product
#
# f[n] = max {
#           c * f[n-c]
#           c * (n-c)
#           f[c] * f[n-c]
#           f[c] * (n-c)
#        }
#        where 1 <= c <= n/2
#
# Solution 2:
#
# based on solution 1, make c in (2, 3)
#

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        #coins = list(range(1, n//2+1))
        coins = [2, 3]
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
