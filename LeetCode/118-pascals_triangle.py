class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = [[1]]
        for i in range(1, numRows):
            rows.append([0] * (i+1))
            rows[i][0] = rows[i-1][0]
            rows[i][i] = rows[i-1][i-1]
            for j in range(1, i):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
        return rows[:numRows]
