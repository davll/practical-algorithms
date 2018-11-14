# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# T = O(n)
def find_min_v0(nums):
    return min(range(len(nums)), key=lambda i: nums[i])

# Worst T = O(n)
# Average T = O(log(n))
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
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = find_min_v1(nums)
        print(str(i))
        return nums[i]
