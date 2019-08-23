#
# Longest Common Subsequence
#
# F[i,j] : longest length of common subsequence of s1[:i] and s2[:j]
#        = 0                           if i = 0 or j = 0
#        = F[i-1,j-1] + 1              if s1[i-1] == s2[j-1]
#        = max { F[i-1,j], F[i,j-1] }  otherwise
#

def lcs_v1(s1, s2):
    n1, n2 = len(s1), len(s2)
    F = [[0] * (n2+1) for _ in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1] == s2[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[n1][n2]

def lcs_v2(s1, s2):
    n1, n2 = len(s1), len(s2)
    F1, F2 = [[0] * (n2+1) for _ in range(2)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1] == s2[j-1]:
                F2[j] = F1[j-1] + 1
            else:
                F2[j] = max(F1[j], F2[j-1])
        F1, F2 = F2, F1
    return F1[-1]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return lcs_v2(text1, text2)
