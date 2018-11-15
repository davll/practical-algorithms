# https://leetcode.com/problems/jump-game-ii/

# Idea: Dynamic Programming
def jump_v1(nums):
    n = len(nums)
    dp = [2*n] * n
    dp[0] = 0
    for i in range(n-1):
        s = nums[i]
        for j in range(i+1, min(n, i+s+1)):
            dp[j] = min(dp[j], dp[i]+1)
    return dp[-1]

# Idea: Greedy (implicit BFS)
def jump_v2(nums):
    jumps, last, farest = 0, 0, 0
    for i, x in enumerate(nums[:len(nums)-1]):
        farest = max(farest, i + x)
        if i == last:
            jumps += 1
            last = farest
    return jumps

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return jump_v2(nums)
