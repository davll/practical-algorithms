class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        reachable = 0
        for i, x in enumerate(nums):
            if x == 0:
                if reachable <= i:
                    break
            else:
                reachable = max(reachable, i + x)
        return reachable >= len(nums)-1
