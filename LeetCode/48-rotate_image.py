class Solution(object):
    def rotate(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(n):
            jl, jr = 0, n-1
            while jl < jr:
                mat[i][jl], mat[i][jr] = mat[i][jr], mat[i][jl]
                jl, jr = jl+1, jr-1
