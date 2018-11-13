class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        # determine if 0-th row should be cleared
        clear_first_row = any(map(lambda x: x == 0, matrix[0]))
        # determine if 0-th column should be cleared
        clear_first_col = any(map(lambda x: x == 0, (matrix[i][0] for i in range(m))))
        # determine if i-th row should be cleared (except 0-th row)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
        # determine if j-th column should be cleared (except 0-th col)
        for j in range(1, n):
            for i in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
        # clearing
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if clear_first_row:
            for j in range(n):
                matrix[0][j] = 0
        if clear_first_col:
            for i in range(m):
                matrix[i][0] = 0
