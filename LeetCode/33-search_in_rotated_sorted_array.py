# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search_v1(nums, target):
    return (list(filter(lambda i: nums[i] == target, range(len(nums)))) + [-1])[0]

def search_v2(nums, target):
    n = len(nums)
    l, r = 0, n-1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            if target <= nums[r]: # M < target <= R => in M..R
                l = m+1
            elif nums[l] <= nums[m]: # R < L <= M < target => in M..R
                r = m-1
            elif nums[m]: # M < R < L => 
        else: # nums[m] > target
            if target >= nums[l]: # L <= target < M
                r = m-1
            # R < L < M => 2 3 1
            # M < R < L => 3 1 2
    return -1

def find_min(nums):
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

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return search_v2(nums, target)
