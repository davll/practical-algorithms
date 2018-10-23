# Maximum Product Subarray
#
# Hint: Dynamic Programming
#
#
#

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        maxdp, mindp = [0]*n, [0]*n
        maxdp[0], mindp[0] = nums[0], nums[0]
        for i in range(1,n):
            a = nums[i] * maxdp[i-1]
            b = nums[i] * mindp[i-1]
            c = nums[i]
            maxdp[i] = max(a, b, c)
            mindp[i] = min(a, b, c)
        return max(maxdp)
