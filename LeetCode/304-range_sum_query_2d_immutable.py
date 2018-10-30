class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.prefix = [m[:] for m in matrix]
        self.m = len(matrix)
        self.n = len(matrix[0]) if matrix else 0
        if self.m == 0 or self.n == 0:
            return
        for i in range(self.m):
            for j in range(1, self.n):
                self.prefix[i][j] += self.prefix[i][j-1]
        for j in range(self.n):
            for i in range(1, self.m):
                self.prefix[i][j] += self.prefix[i-1][j]
        #for i in range(1, self.m):
        #    self.prefix[i][0] += self.prefix[i-1][0]
        #    for j in range(1, self.n):
        #        self.prefix[i][j] += self.prefix[i][j-1] + self.prefix[i-1][j] - self.prefix[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        def prefix(i, j):
            if i >= 0 and j >= 0:
                return self.prefix[i][j]
            else:
                return 0
        return prefix(row2, col2) - prefix(row1-1, col2) - prefix(row2, col1-1) + prefix(row1-1, col1-1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
