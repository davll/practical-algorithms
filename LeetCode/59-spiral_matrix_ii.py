# https://leetcode.com/problems/spiral-matrix-ii/

def spiral_fill(n):
    mat = [[0] * n for _ in range(n)]
    i, j = 0, 0
    mat[i][j] = 1
    repeat = True
    while repeat:
        repeat = False
        # +j direction
        while j+1 < n and mat[i][j+1] == 0:
            mat[i][j+1] = mat[i][j] + 1
            j = j + 1
            repeat = True
        # +i direction
        while i+1 < n and mat[i+1][j] == 0:
            mat[i+1][j] = mat[i][j] + 1
            i = i + 1
            repeat = True
        # -j direction
        while j-1 >= 0 and mat[i][j-1] == 0:
            mat[i][j-1] = mat[i][j] + 1
            j = j - 1
            repeat = True
        # -i direction
        while i-1 >= 0 and mat[i-1][j] == 0:
            mat[i-1][j] = mat[i][j] + 1
            i = i - 1
            repeat = True
    return mat

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return spiral_fill(n)
