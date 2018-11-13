# https://leetcode.com/problems/word-search/

def backtrack(board, word, x, i, j, m, n, visited):
    if x == len(word):
        return True
    if i < 0 or i >= m or j < 0 or j >= n:
        return False
    if visited[i][j] or word[x] != board[i][j]:
        return False
    visited[i][j] = True
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if backtrack(board, word, x+1, i+di, j+dj, m, n, visited):
            return True
    visited[i][j] = False
    return False

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return len(word) == 0
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if backtrack(board, word, 0, i, j, m, n, visited):
                    return True
        return False
