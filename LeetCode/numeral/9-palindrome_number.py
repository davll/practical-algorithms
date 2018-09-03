def copysign(x,y):
    x = abs(x)
    if y >= 0:
        return x
    else:
        return -x

def reverse(x):
    # check
    if x > (2**31-1) or x < -(2**31):
        return 0
    # compute
    tmp, result = abs(x), 0
    while tmp > 0:
        result = (result * 10) + (tmp % 10)
        tmp = tmp // 10
    return copysign(result, x)

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = reverse(x)
        return (x == y)
