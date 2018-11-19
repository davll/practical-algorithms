# https://leetcode.com/problems/longest-harmonious-subsequence/description/

from collections import Counter

def lhs_v1(nums):
    count = Counter(nums)
    result = 0
    for x, n in count.items():
        m = count[x+1]
        if m > 0:
            result = max(result, n + m)
    return result

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return lhs_v1(nums)
