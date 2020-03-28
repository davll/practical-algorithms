# https://leetcode.com/problems/find-peak-element/

from math import inf

def find_peak_v1(nums):
    n = len(nums)
    nums = [-inf] + nums + [-inf]
    for i in range(1, n+1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i-1

def find_peak_v2(nums):
    n = len(nums)
    nums = [-inf] + nums + [-inf]
    l, r = 1, n+1
    while l <= r:
        m = (l + r) // 2
        if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
            return m-1
        elif nums[m-1] < nums[m] and nums[m] < nums[m+1]:
            l, r = m+1, r
        else:
            l, r = l, m-1
    return l-1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return find_peak_v2(nums)
