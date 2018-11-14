# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def search_v0(nums, target):
    return target in nums

def search_v1(nums, target):
    s = find_min_v1(nums)
    n = len(nums)
    l, r = 0, n-1
    while l <= r:
        m = (l + r) // 2
        if nums[(m+s)%n] == target:
            return True
        elif nums[(m+s)%n] < target:
            l = m+1
        else:
            r = m-1
    return False

def find_min_v1(nums):
    n = len(nums)
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m+1
        elif nums[m] < nums[r]:
            r = m
        else:
            while l < r and nums[m] == nums[r-1]:
                r -= 1
            while l < r and nums[m] == nums[l]:
                l += 1
    return l

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return search_v1(nums, target)
