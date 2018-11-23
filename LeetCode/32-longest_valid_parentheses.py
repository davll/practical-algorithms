# https://leetcode.com/problems/longest-valid-parentheses/

# Idea: Dynamic Programming
#
# F[i,j] = whether S[i]..S[j] forms valid parentheses
#
# F[i,i] = False
# F[i,i+1] = True if S[i] = '(' and S[i+1] = ')'
# F[i,j] = or {
#             F[i+1,j-1]           if S[i] = '(' and S[j] = ')'
#             F[i,k] and F[k+1,j]  for i <= k < k
#          }
#
def lvp_v1(S):
    N = len(S)
    F = [[False] * N for _ in range(N)]
    for i in range(N-1):
        F[i][i+1] = (S[i] == '(' and S[i+1] == ')')
    for m in range(4, N+1, 2):
        for i in range(N-m+1):
            j = i + m - 1
            if S[i] == '(' and S[j] == ')':
                F[i][j] = F[i+1][j-1]
            for k in range(i, j):
                F[i][j] = F[i][j] or (F[i][k] and F[k+1][j])
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            if F[i][j]:
                result = max(result, j-i+1)
    return result

# Idea: Dynamic Programming
#
# P[i] = the longest length of valid parentheses ending at S[i]
#
# P[0] = 0
#
# P[1] = 2 if S[0] = '(' and S[1] = ')'
#        0 otherwise
#
# P[i] = P[i-2] + 2 if S[i-1] = '(' and S[i] = ')'
#        P[j-1] + P[i-1] + 2 if S[j] = '(' and S[i] = ')' where j = i-1-P[i-1]
#
def lvp_v2(S):
    N = len(S)
    P = [0] * N
    if N < 2:
        return 0
    for i in range(1, N):
        if S[i-1] == '(' and S[i] == ')':
            if i >= 2:
                P[i] = P[i-2] + 2
            else:
                P[i] = 2
        j = i - 1 - P[i-1]
        if j >= 0:
            if S[j] == '(' and S[i] == ')':
                if j > 0:
                    P[i] = max(P[i], P[j-1] + P[i-1] + 2)
                else:
                    P[i] = max(P[i], P[i-1] + 2)
    return max(P)

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return lvp_v2(s)
