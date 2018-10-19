def count_trees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for k in range(1,n+1):
        x = 0
        for j in range(1,k+1):
            x += dp[j-1] * dp[k-j]
        dp[k] = x
    return dp[n]

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return count_trees(n)
