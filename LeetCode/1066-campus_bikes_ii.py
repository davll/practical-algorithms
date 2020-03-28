from math import inf

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# TLE...
def assign_bikes_v1(workers, bikes):
    m, n = len(workers), len(bikes)
    assignment = [-1] * m
    used = [False] * n
    def backtrack(i):
        if i < m:
            ans = inf
            for j in range(n):
                if not used[j]:
                    used[j] = True
                    assignment[i] = j
                    ans = min(ans, backtrack(i+1))
                    used[j] = False
            return ans
        else:
            ans = 0
            for i, j in enumerate(assignment):
                ans += manhattan(workers[i], bikes[j])
            return ans
    return backtrack(0)

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

# https://leetcode.com/problems/campus-bikes-ii/discuss/412367/Java-Plain-DFS-And-DP-Solution-with-Video-Explanation
# https://leetcode.com/problems/campus-bikes-ii/discuss/435944/Reduce-2D-dp-to-1D-dp
# https://leetcode.com/problems/campus-bikes-ii/discuss/430013/Beats-95-in-time-100-in-memory-(DFS-%2B-DP)
# https://leetcode.com/problems/campus-bikes-ii/discuss/391714/C%2B%2B-Dijkstra's-Algorithm-with-Detailed-Comments
# https://leetcode.com/problems/campus-bikes-ii/discuss/404947/Python-top-down-DP-beats-93.02-with-explanation
# https://leetcode.com/problems/campus-bikes-ii/discuss/408311/Easy-python-solution-97
# https://leetcode.com/problems/campus-bikes-ii/discuss/416452/Python-runtime-beats-100-min-cost-bipartite-matching.

