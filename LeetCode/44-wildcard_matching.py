# https://leetcode.com/problems/wildcard-matching/

# Idea: Dynamic Programming
#
# F[i,j]: the matching status of S[:i] and P[:j]
#
# F[0,0] = True
# F[0,j] = F[0,j-1]             if P[j-1] == '*'
#
# F[i,j] = F[i-1,j-1]           if S[i-1] == P[j-1] or P[j-1] == '?'
#        = F[i,j-1]             if P[j-1] == '*'
#

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                f[0][j] = f[0][j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    f[i][j] = f[i-1][j-1]
                elif p[j-1] == '*':
                    f[i][j] = f[i][j-1] or f[i-1][j]
        return f[m][n]
