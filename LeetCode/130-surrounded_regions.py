from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        # replace 'O' with 'A'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'A'
        # do bfs
        q = deque()
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == 'A':
                    q.append((i,j))
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'A':
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            if i < 0 or i >= m or j < 0 or j >= n:
                continue
            if board[i][j] != 'A':
                continue
            board[i][j] = 'O'
            q.append((i-1,j))
            q.append((i+1,j))
            q.append((i,j-1))
            q.append((i,j+1))
        # replace 'A' with 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'X'

