def combine_v1(n, k):
    buf = [-1] * k
    def backtrack(i):
        if i < k:
            s = 1 if i == 0 else buf[i-1]+1
            for x in range(s, n+1):
                buf[i] = x
                yield from backtrack(i+1)
        else:
            yield buf[:]
    return list(backtrack(0))

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return combine_v1(n, k)
