# https://leetcode.com/problems/regular-expression-matching/
# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest

# Idea: Dynamic Programming
#
# F[i][j]: the matching status of S[:i] and P[:j]
# F[0][0] = True
# F[1][1] = S[0] == P[0]
#
# F[0][j] = F[0][j-2]                               if P[j-1] == '*'
#
# F[i][j] = {                                       if P[j-1] == '*'
#              F[i][j-2]
#              or F[i][j-1]
#              or F[i-1][j]      if P[j-2] == '.' or P[j-2] == S[i-1]
#           }
#         = F[i-1][j-1]                             if P[j-1] == '.'
#         = F[i-1][j-1] and S[i-1] == P[j-1]        otherwise
#
def check_match_v2(s, p):
    m, n = len(s), len(p)
    f = [[False] * (n+1) for _ in range(m+1)]
    # compare two empty strings
    f[0][0] = True
    # compare S[:0] with P[:j]
    for j in range(2, n+1):
        f[0][j] = f[0][j-2] and p[j-1] == '*'
    # 
    for j in range(1, n+1):
        for i in range(1, m+1):
            if p[j-1] == '*':
                # Eliminations: Try P[:j-2] or P[:j-1] (without *)
                f[i][j] = f[i][j-2] or f[i][j-1]
                # Propagations: check if S[:i] matches P[:j-1]
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    f[i][j] = f[i][j] or f[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                f[i][j] = f[i-1][j-1]
    #
    return f[m][n]

class Solution(object):
    def isMatch(self, s, t):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return check_match_v2(s, t)

# testcase 1: r/a*a/
