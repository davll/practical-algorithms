# https://leetcode.com/problems/shortest-path-to-get-all-keys/

from heapq import heappush, heappop
from collections import defaultdict
from math import inf

# Idea: BFS + Dijkstra
#
# state = (steps, keys, position)
#
def shortest_path_v1(grid):
    m, n = len(grid), len(grid[0])
    goal = all_keys(grid, m, n)
    si, sj = find_starting_point(grid, m, n)
    costs = defaultdict(lambda: inf)
    costs[0, si, sj] = 0
    # entry: (steps, keys, position)
    queue = [(0, 0, si, sj)]
    while queue:
        steps, keys, i, j = heappop(queue)
        if steps > costs[keys, i, j]:
            continue
        if keys == goal:
            return steps
        for ti, tj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if ti not in range(m):
                continue
            if tj not in range(n):
                continue
            if check_wall(grid, ti, tj):
                continue
            if check_lock(grid, ti, tj, keys):
                continue
            k = check_key(grid, ti, tj, keys)
            if steps + 1 < costs[k, ti, tj]:
                heappush(queue, (steps+1, k, ti, tj))
                costs[k, ti, tj] = steps + 1
    return -1

def find_starting_point(grid, m, n):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                return (i, j)
    raise ValueError('The grid does not have any starting point')

def all_keys(grid, m, n):
    bits = 0
    for i in range(m):
        for j in range(n):
            c = ord(grid[i][j]) - ord('a')
            if c in range(26):
                bits = bits | (1 << c)
    return bits

def check_wall(grid, i, j):
    return grid[i][j] == '#'

def check_lock(grid, i, j, keys):
    c = ord(grid[i][j]) - ord('A')
    if c not in range(26):
        return False
    return (keys & (1 << c)) == 0

def check_key(grid, i, j, keys):
    c = ord(grid[i][j]) - ord('a')
    if c not in range(26):
        return keys
    return keys | (1 << c)

class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        return shortest_path_v1(grid)
