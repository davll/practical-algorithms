def copysign(x,y):
    x = abs(x)
    if y >= 0:
        return x
    else:
        return -x

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # check
        if x > (2**31-1) or x < -(2**31):
            return 0
        # compute
        tmp, result = abs(x), 0
        while tmp > 0:
            result = (result * 10) + (tmp % 10)
            tmp = tmp // 10
        result = copysign(result, x)
        # check overflow
        if result > (2**31-1) or result < -(2**31):
            return 0
        else:
            return result

"""
if __name__ == "__main__":
    x = int(input("enter a number "))
    print("input = " + str(x))
    s = Solution()
    y = s.reverse(x)
    print("ans = " + str(y))
"""
