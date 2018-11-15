def spiral_fill(n):
    mat = [[0] * n for _ in range(n)]
    row0, row1, col0, col1 = 0, n-1, 0, n-1

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return spiral_fill(n)
