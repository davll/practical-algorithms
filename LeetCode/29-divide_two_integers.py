# https://leetcode.com/problems/divide-two-integers/

def div_int(x, y):
    s = 0
    q = 0
    # find max s
    while x >= (y << (s+1)):
        s = s + 1
    while s >= 0:
        q = q << 1
        if x >= (y << s):
            q = q | 1
            x = x - (y << s)
        s -= 1
    return q

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        q = div_int(abs(dividend), abs(divisor))
        if neg:
            if q > 2**31:
                q = 2**31
            return -q
        else:
            if q > 2**31 - 1:
                q = 2**31 - 1
            return q
