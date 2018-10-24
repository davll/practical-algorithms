def square_root(x):
    l, r = 0, x
    result = 0
    while l <= r:
        m = (l + r) // 2
        sm = m * m
        if sm == x:
            result = m
            break
        elif sm < x:
            result = m
            l = m+1
        else: # sm > x
            r = m-1
    return result

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return square_root(x)

#for i in range(1, 17):
#    print("sqrt({i}) = {x}".format(i=i, x=square_root(i)))
