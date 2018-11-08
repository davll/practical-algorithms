# https://leetcode.com/problems/regular-expression-matching/
# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
# https://knightzone.studio/2018/09/30/3644/leetcode%EF%BC%9A10-regular-expression-matching/

# Idea: Non-deterministic Finite Automata
def check_match_v1(S, P):
    pass

# Idea: Dynamic Programming
#
# F[i][j] = S[:i] matches P[:j]
# F[0][0] = True
# F[1][1] = S[0] == P[0]
#
# F[0][j] = F[0][j-2]                               if P[j-1] == '*'
#
# F[i][j] = {                                       if P[j-1] == '*'
#              F[i][j-2]        # S[:i] matches P[:j-2] (without .*)
#              or F[i][j-1]     # S[:i] matches P[:j-1] (without *)
#              or F[i-1][j]     if P[j-2] == '.' or P[j-2] == S[i-1]
#           }
#         = F[i-1][j-1]                             if P[j-1] == '.'
#         = F[i-1][j-1] and S[i-1] == P[j-1]        otherwise
#
def check_match_v2(S, P):
    m, n = len(S), len(P)
    F = [[False] * (n+1) for _ in range(m+1)]
    # compare two empty strings
    F[0][0] = True
    # compare S[:0] with P[:j]
    for j in range(2, n+1):
        F[0][j] = F[0][j-2] and P[j-1] == '*'
    # 
    for j in range(1, n+1):
        for i in range(1, m+1):
            if P[j-1] == '*':
                # Eliminations: Try P[:j-2] or P[:j-1] (without *)
                F[i][j] = F[i][j-2] or F[i][j-1]
                # Propagations: check if S[:i] matches P[:j-1]
                if P[j-2] == '.' or P[j-2] == S[i-1]:
                    F[i][j] = F[i][j] or F[i-1][j]
            elif P[j-1] == '.' or P[j-1] == S[i-1]:
                F[i][j] = F[i-1][j-1]
    #
    return F[m][n]

class Solution(object):
    def isMatch(self, s, t):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return check_match_v2(s, t)

# testcase 1: r/a*a/
