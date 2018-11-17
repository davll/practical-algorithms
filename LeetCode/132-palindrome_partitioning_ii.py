# https://leetcode.com/problems/palindrome-partitioning-ii/

# Idea: Dynamic Programming
#
# P[i,j]: whether S[i]..S[j] is palindrome
# F[i,j]: minimum cut of S[i]..S[j]
#
# P[i,i] = True
# P[i,i+1] = S[i] == S[i+1]
# P[i,j] = S[i] == S[j] and P[i+1,j-1]
#
# F[i,j] = 0                                if P[i,j] = True
#          min { F[i,k] + F[k+1,j] + 1 }    otherwise
#               where k = i .. j-1
#
# => T = O(n^3) => too slow!
#
# => Optimize!
#
# C[i]: minimum cut of S[0] .. S[i]
#
# C[0] = 0
# C[i] = 0    if P[0][i] = True
#        min { C[j] + 1 if P[j,i] = True } for all j in 0..i-1  
#
# => T = O(n^2)
#

def min_cut_v1(S):
    n = len(S)
    P = find_palindromes(S)
    F = [[n] * n for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    for i in range(n-1):
        F[i][i+1] = 1 - int(P[i][i+1])
    for d in range(3, n+1):
        for i in range(n-d+1):
            j = i + d - 1
            if P[i][j]:
                F[i][j] = 0
            else:
                for k in range(i, j):
                    F[i][j] = min(F[i][j], F[i][k]+F[k+1][j]+1)
    return F[0][n-1]

def min_cut_v2(S):
    n = len(S)
    P = find_palindromes(S)
    C = [n] * n
    for i in range(n):
        if P[0][i]:
            C[i] = 0
        else:
            for j in range(i):
                if P[j+1][i]:
                    C[i] = min(C[i], 1 + C[j])
    return C[n-1]

def find_palindromes(S):
    n = len(S)
    P = [[False] * n for _ in range(n)]
    for i in range(n):
        P[i][i] = True
    for i in range(n-1):
        P[i][i+1] = S[i] == S[i+1]
    for d in range(3, n+1):
        for i in range(n-d+1):
            j = i + d - 1
            P[i][j] = (S[i] == S[j] and P[i+1][j-1])
    return P

class Solution:
    def minCut(self, S):
        """
        :type S: str
        :rtype: int
        """
        return min_cut_v2(S)
