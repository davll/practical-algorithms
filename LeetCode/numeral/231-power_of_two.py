def lsb(n):
    return n & (-n)

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            return n == lsb(n)
