# Kadane's Algorithm
#
# If we know the maximum subarray sum ending at position i (aka nums[i]),
# what is the maximum subarray sum ending at position i+1?
#
# ans[i+1] = max { nums[i+1] ; nums[i+1] + ans[i] }
#
# https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
#
def maxsum_dp(nums):
    for i in range(1, len(nums)):
        nums[i] += max(0, nums[i-1])
    return max(nums)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return maxsum_dp(nums)
