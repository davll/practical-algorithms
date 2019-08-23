from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        #
        q = deque()
        p = 0
        # find rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i+1,j,1))
                    q.append((i-1,j,1))
                    q.append((i,j-1,1))
                    q.append((i,j+1,1))
        # propagate
        while q:
            i, j, t = q.popleft()
            if i < 0 or i >= m or j < 0 or j >= n:
                continue
            if grid[i][j] != 1:
                continue
            p = max(p, t)
            grid[i][j] = 2
            q.append((i+1,j, t+1))
            q.append((i-1,j, t+1))
            q.append((i,j-1, t+1))
            q.append((i,j+1, t+1))
        # return -1 if there are fresh oranges left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        # otherwise, return the answer
        return p
