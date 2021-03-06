# https://leetcode.com/problems/house-robber/description/

# Idea: Dynamic Programming
#
# F[i] = maximum amount of money after robbing A[:i]
#
# F[0] = 0
# F[i] = max(F[i-1], F[i-2] + A[i-1])
#

def rob_v1(A):
    n = len(A)
    F = [0] * (n+1)
    for i in range(1, n+1):
        F[i] = max(F[i-1], F[i-2] + A[i-1])
    return F[n]

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return rob_v1(nums)
