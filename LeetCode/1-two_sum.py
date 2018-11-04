def two_sum_v1(nums, target):
    lut = {}
    for i in range(len(nums)):
        if nums[i] in lut:
            return [lut[nums[i]], i]
        else:
            lut[target - nums[i]] = i

def two_sum_v2(nums, target):
    pass

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
