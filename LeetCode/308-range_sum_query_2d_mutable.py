class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.rows = m
        self.cols = n
        self.tree = [[0] * n for _ in range(m)]
        self.data = matrix
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                self._update(i, j, x)
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.data[row][col]
        self.data[row][col] = val
        self._update(row, col, delta)
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        a11 = self._query(row2, col2)
        a10 = self._query(row2, col1-1)
        a01 = self._query(row1-1, col2)
        a00 = self._query(row1-1, col1-1)
        return a11 + a00 - a10 - a01
    # update A[i][j]
    def _update(self, i, j, delta):
        m, n = self.rows, self.cols
        i, j = i+1, j+1
        i0, j0 = i, j
        while i <= m:
            j = j0
            while j <= n:
                self.tree[i-1][j-1] += delta
                j += _lsb(j)
            i += _lsb(i)
    # returns A[0][0] + ... + A[0][j] +
    #           ...            ...    +
    #         A[i][0] + ... + A[i][j]
    def _query(self, i, j):
        i, j = i+1, j+1
        i0, j0 = i, j
        result = 0
        while i > 0:
            j = j0
            while j > 0:
                result += self.tree[i-1][j-1]
                j -= _lsb(j)
            i -= _lsb(i)
        return result

def _lsb(x):
    return x & (-x)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
