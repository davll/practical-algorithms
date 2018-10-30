class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.fsum = [0] * (len(nums)+1)
        for i, x in enumerate(nums):
            self.update(i, x)
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        n = len(self.fsum)
        i = i + 1
        while i <= n:
            self.fsum[i] += val
            i += _lsb(i)
    def query(self, i):
        i = i + 1
        result = 0
        while i >= 1:
            result += self.fsum[i]
            i -= _lsb(i)
        return result
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(j) - self.query(i-1)

def _lsb(x):
    return x & (-x)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
