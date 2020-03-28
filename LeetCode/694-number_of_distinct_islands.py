from collections import deque

def num_distinct_islands_v1(grid):
    m = len(grid)
    n = len(grid[0])
    islands = set()
    # bfs
    mark = [[0] * n for _ in range(m)]
    queue = deque()
    for si in range(m):
        for sj in range(n):
            if grid[si][sj] != 1 or mark[si][sj] != 0:
                continue
            # bounds
            imin, imax, jmin, jmax = m, -1, n, -1
            mark[si][sj] = 1
            queue.append((si, sj))
            while queue:
                i, j = queue.popleft()
                assert mark[i][j] == 1
                imin = min(imin, i)
                imax = max(imax, i)
                jmin = min(jmin, j)
                jmax = max(jmax, j)
                if i < m-1 and grid[i+1][j] == 1 and mark[i+1][j] == 0:
                    mark[i+1][j] = 1
                    queue.append((i+1,j))
                if i > 0 and grid[i-1][j] == 1 and mark[i-1][j] == 0:
                    mark[i-1][j] = 1
                    queue.append((i-1,j))
                if j < n-1 and grid[i][j+1] == 1 and mark[i][j+1] == 0:
                    mark[i][j+1] = 1
                    queue.append((i,j+1))
                if j > 0 and grid[i][j-1] == 1 and mark[i][j-1] == 0:
                    mark[i][j-1] = 1
                    queue.append((i,j-1))
            # 
            canvas = [[0] * (jmax - jmin + 1) for _ in range(imax - imin + 1)]
            mark[si][sj] = 2
            queue.append((si, sj))
            while queue:
                i, j = queue.popleft()
                assert mark[i][j] == 2
                canvas[i-imin][j-jmin] = 1
                if i < m-1 and mark[i+1][j] == 1:
                    mark[i+1][j] = 2
                    queue.append((i+1,j))
                if i > 0 and mark[i-1][j] == 1:
                    mark[i-1][j] = 2
                    queue.append((i-1,j))
                if j < n-1 and mark[i][j+1] == 1:
                    mark[i][j+1] = 2
                    queue.append((i,j+1))
                if j > 0 and mark[i][j-1] == 1:
                    mark[i][j-1] = 2
                    queue.append((i,j-1))
            #
            canvas = ';'.join(''.join(map(str, row)) for row in canvas)
            islands.add(canvas)
    #
    return len(islands)

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        return num_distinct_islands_v1(grid)
