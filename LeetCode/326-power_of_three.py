from math import ceil, log

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and pow(3, ceil(log(float(n), 3))) == n
