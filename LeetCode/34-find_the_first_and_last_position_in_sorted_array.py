# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def find_first(nums, target):
    l, r = 0, len(nums)-1
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            pos = m
            r = m-1
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    return pos

def find_last(nums, target):
    l, r = 0, len(nums)-1
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            pos = m
            l = m+1
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    return pos

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = find_first(nums, target)
        last = find_last(nums, target)
        return [first, last]
