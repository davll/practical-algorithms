def decomp(x):
    while x > 0:
        yield x % 10
        x = x // 10

def count(nums):
    prev, n = None, 0
    for y in nums:
        for x in decomp(y):
            if prev is not None and prev != x:
                yield from (n, prev)
                n = 0
            prev = x
            n += 1
    if prev is not None:
        yield from (n, prev)

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = [1]
        for _ in range(2,n+1):
            x = list(count(x))
        return ''.join(map(str,x))
