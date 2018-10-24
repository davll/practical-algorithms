def pos_power(x, n):
    y = 1
    while n > 0:
        if n % 2 == 1:
            y *= x
        n //= 2
        x = x * x
    return y

def neg_power(x, n):
    y = 1
    n = -n
    x = 1 / x
    while n > 0:
        if n % 2 == 1:
            y *= x
        n //= 2
        x = x * x
    return y

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n >= 0:
            return pos_power(x, n)
        else:
            return neg_power(x, n)
