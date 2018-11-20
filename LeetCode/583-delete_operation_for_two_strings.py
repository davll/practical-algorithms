# https://leetcode.com/problems/delete-operation-for-two-strings/description/
# https://leetcode.com/articles/delete-operation-for-two-strings/

# Idea: Dynamic Programming => find LCS
def lcs(A, B):
    m, n = len(A), len(B)
    L = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j], L[i-1][j-1])
    return L[m][n]

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = lcs(word1, word2)
        return len(word1) + len(word2) - 2 * s
