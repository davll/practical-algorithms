from math import log2, floor

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        p = floor(log2(n) / log2(5))
        count = 0
        for i in range(1,p+1):
            count += n // (5 ** i)
        return count
