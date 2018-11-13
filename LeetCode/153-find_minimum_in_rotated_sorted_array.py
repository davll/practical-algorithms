# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def find_min_v0(nums):
    return min(range(len(nums)), key=lambda i: nums[i])

def find_min_v1(nums):
    n = len(nums)
    l, r = 0, n-1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m+1
        elif nums[m] < nums[r]:
            r = m
        else:
            return m
    return -1

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums[find_min_v1(nums)]
