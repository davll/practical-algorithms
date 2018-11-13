# https://leetcode.com/problems/first-missing-positive/

from heapq import heapify, heappop

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = 1
        heapify(nums)
        while nums:
            x = heappop(nums)
            if x == expected:
                expected += 1
        return expected
