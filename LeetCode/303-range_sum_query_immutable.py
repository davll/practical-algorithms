class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        prefix = nums[:]
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        self.prefix = prefix
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.prefix[j]
        else:
            return self.prefix[j] - self.prefix[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
