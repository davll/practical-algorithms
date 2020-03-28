from math import inf

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def assign_bikes_v2(workers, bikes):
    m, n = len(workers), len(bikes)
    # m, n: 1 ~ 10
    memo = dict()
    #used = 0b0000000000
    def mark_used(used, j):
        return (used | (0x1 << j))
    def is_used(used, j):
        return (used & (0x1 << j)) != 0
    def backtrack(used, i):
        if i < m:
            key = (i, used)
            if key in memo:
                return memo[key]
            tmp = inf
            for j in range(n):
                if not is_used(used, j):
                    d = manhattan(workers[i], bikes[j])
                    tmp = min(tmp, d + backtrack(mark_used(used, j), i+1))
            memo[key] = tmp
            return tmp
        else:
            return 0
    return backtrack(0, 0)

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        return assign_bikes_v2(workers, bikes)
