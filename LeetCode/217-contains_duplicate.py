class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        nums.sort()
        prev = nums[0]
        for x in nums[1:]:
            if prev == x:
                return True
            prev = x
        return False
