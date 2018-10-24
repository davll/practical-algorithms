# https://leetcode.com/articles/next-permutation/

def nextperm(nums):
    i = len(nums)-2
    # find 1st number which is smaller than its following number
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    # nums[i+1:] is in descending order
    if i >= 0:
        for j in range(len(nums)-1, i, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
    # reverse
    l, r = i+1, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r-1

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nextperm(nums)
