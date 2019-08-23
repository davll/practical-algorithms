from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2 ** 31 - 1
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        if n == 0:
            return
        # bfs
        q = deque()
        # find gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i+1, j, 1))
                    q.append((i-1, j, 1))
                    q.append((i, j+1, 1))
                    q.append((i, j-1, 1))
        # propagate
        while q:
            i, j, d = q.popleft()
            if i < 0 or i >= m or j < 0 or j >= n:
                continue
            if rooms[i][j] <= d:
                continue
            rooms[i][j] = d
            q.append((i+1, j, d+1))
            q.append((i-1, j, d+1))
            q.append((i, j+1, d+1))
            q.append((i, j-1, d+1))

