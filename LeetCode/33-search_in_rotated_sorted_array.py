# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search_v1(nums, target):
    return (list(filter(lambda i: nums[i] == target, range(len(nums)))) + [-1])[0]

def search_v2(nums, target):
    n = len(nums)
    s = find_min(nums)
    assert s >= 0
    l, r = 0, n-1
    while l <= r:
        m = (l + r) // 2
        if nums[(m+s)%n] == target:
            return (m+s)%n
        elif nums[(m+s)%n] < target:
            l = m+1
        else:
            r = m-1
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
