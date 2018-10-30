class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = 0
        i = 32
        while i > 0:
            x = (x << 1) | (n & 1)
            n = n >> 1
            i -= 1
        return x
