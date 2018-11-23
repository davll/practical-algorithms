# https://leetcode.com/problems/combinations/

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

def combine_v1a(n, k):
    def backtrack(n, k):
        if k == 0:
            yield []
        else:
            for i in range(k, n+1):
                for pre in backtrack(i-1, k-1):
                    yield pre + [i]
    return list(backtrack(n, k))

def combine_v2(n, k):
    if k == 0:
        return [[]]
    return [pre + [i] for i in range(k, n+1) for pre in combine_v2(i-1, k-1)]

def combine_v3(n, k):
    combs = [[]]
    for _ in range(k):
        combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
    return combs

def combine_v4(n, k):
    from itertools import combinations
    return list(combinations(range(1, n+1), k))

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return combine_v1a(n, k)
