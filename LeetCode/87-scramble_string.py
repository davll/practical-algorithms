# https://leetcode.com/problems/scramble-string/

#
# F[l][i][j] : s1[i:i+l] & s2[j:j+l] are scramble
#

def is_scramble(s1, s2):
    assert len(s1) == len(s2)
    n = len(s1)
    F = [[[False] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            F[0][i][j] = s1[i] == s2[j]
    for l in range(1,n):
        for i in range(n-l):
            for j in range(n-l):
                tmp = False
                for k in range(l):
                    tmp = tmp or (F[k][i][j] and F[l-k-1][i+k+1][j+k+1])
                    tmp = tmp or (F[k][i][j+l-k] and F[l-k-1][i+k+1][j])
                F[l][i][j] = tmp
    return F[-1][0][0]

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return is_scramble(s1, s2)
