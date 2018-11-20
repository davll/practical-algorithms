# https://leetcode.com/problems/house-robber-ii/

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
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(rob_v1(nums[:-1]), rob_v1(nums[1:]))
