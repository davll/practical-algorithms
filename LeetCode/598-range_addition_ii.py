# https://leetcode.com/problems/range-addition-ii/

import numpy as np

def max_count_v1(m, n, ops):
    if not ops:
        return m * n
    A = np.zeros((m, n), dtype='int')
    for i, j in ops:
        A[i-1,j-1] += 1
    # i = m-1
    for j in range(n-2, -1, -1):
        A[m-1,j] += A[m-1,j+1]
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            A[i][j] += max(A[i+1,j], A[i,j+1], A[i+1,j+1])
    x = np.max(A)
    c = 0
    for i in range(m):
        for j in range(n):
            if x == A[i,j]:
                c += 1
    return c

def max_count_v2(m, n, ops):
    p, q = m, n
    for i, j in ops:
        p = min(p, i)
        q = min(q, j)
    return p * q

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return max_count_v2(m, n, ops)
