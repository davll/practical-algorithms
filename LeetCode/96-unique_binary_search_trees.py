# https://leetcode.com/problems/unique-binary-search-trees/

def count_trees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for k in range(1,n+1):
        #
        #   (X)
        #   / \
        #  A   B
        #
        # A = subtree composed of 1 .. X-1
        # B = subtree composed of X+1 .. K
        dp[k] = sum((dp[x-1] * dp[k-x] for x in range(1,k+1)), 0)
    return dp[n]

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return count_trees(n)
