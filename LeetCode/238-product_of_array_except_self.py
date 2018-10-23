class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        tmp = 1
        for i in range(n):
            result[i] *= tmp
            tmp *= nums[i]
        tmp = 1
        for i in reversed(range(n)):
            result[i] *= tmp
            tmp *= nums[i]
        return result
