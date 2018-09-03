class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lut = {}
        for i in range(len(nums)):
            if nums[i] in lut:
                return [lut[nums[i]], i]
            else:
                lut[target - nums[i]] = i
