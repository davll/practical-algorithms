# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

# Idea: Dynamic Programming
def lcis_v1(A):
    n = len(A)
    L = [1] * n
    for i in range(1,n):
        if A[i-1] < A[i]:
            L[i] = L[i-1] + 1
        else:
            L[i] = 1
    return max(L, default=0)

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return lcis_v1(nums)
