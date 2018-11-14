# https://leetcode.com/problems/search-insert-position/

def upper_bound(nums, target):
    n = len(nums)
    l, r = 0, n
    result = n
    while l < r:
        m = (l + r) // 2
        if target < nums[m]:
            result = m
            r = m
        elif target == nums[m]:
            result = m
            r = m-1
        else:
            l = m + 1
    return result

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return upper_bound(nums, target)
