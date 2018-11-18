# https://leetcode.com/problems/max-area-of-island/

from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        return max_island_v1(grid, m, n)

# BFS
def max_island_v1(grid, m, n):
    max_area = 0
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j] or grid[i][j] != 1:
                continue
            visited[i][j] = True
            queue = deque([(i, j)])
            area = 1
            while queue:
                i, j = queue.popleft()
                for ti, tj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    if ti < 0 or ti >= m or tj < 0 or tj >= n:
                        continue
                    if visited[ti][tj] or grid[ti][tj] != 1:
                        continue
                    area += 1
                    visited[ti][tj] = True
                    queue.append((ti, tj))
            max_area = max(area, max_area)
    return max_area
