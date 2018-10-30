class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.size = len(nums)
        self.fsum = [0] * self.size
        for i, x in enumerate(nums):
            self._update(i, x)
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[i]
        self.arr[i] = val
        self._update(i, delta)
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._query(j) - self._query(i-1)
    # update A[i]
    def _update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        n = self.size
        i = i + 1
        while i <= n:
            self.fsum[i-1] += val
            i += _lsb(i)
    # returns A[0] + ... + A[i]
    def _query(self, i):
        i = i + 1
        result = 0
        while i >= 1:
            result += self.fsum[i-1]
            i -= _lsb(i)
        return result

def _lsb(x):
    return x & (-x)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
