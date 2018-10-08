# Longest Common SubSequence
#
# f(i,j) = LCS of A[0:i] and B[0:j]
#
# f(i,j) = []                                     if i = 0 or j = 0
#        = f(i-1,j-1) + [A[i-1]]                  if A[i-1] = B[j-1]
#        = max { f(i-1,j), f(i,j-1), f(i-1,j-1) } otherwise
#

# T = O(nm)
def lcs(A, B):
    m, n = len(A), len(B)
    sz = [[0] * (n+1) for _ in range(m+1)]
    p = [[(i,j) for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                sz[i][j] = sz[i-1][j-1] + 1
                p[i][j] = (i-1, j-1)
            else:
                if sz[i-1][j] > sz[i][j-1]:
                    sz[i][j] = sz[i-1][j]
                    p[i][j] = (i-1, j)
                else:
                    sz[i][j] = sz[i][j-1]
                    p[i][j] = (i, j-1)
    result = []
    while m > 0 and n > 0:
        i, j = p[m][n]
        if A[m-1] == B[n-1]:
            result.append(A[m-1])
        m, n = i, j
    result.reverse()
    return result
