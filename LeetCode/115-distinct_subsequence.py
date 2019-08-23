#
#
#

def num_distinct_subseq(s, t):
    ns, nt = len(s), len(t)
    F = [[0] * (nt+1) for _ in range(ns+1)]
    for i in range(ns+1):
        F[i][0] = 1
    for i in range(1,ns+1):
        for j in range(1,nt+1):
            if s[i-1] == t[j-1]:
                F[i][j] = F[i-1][j] + F[i-1][j-1]
            else:
                F[i][j] = F[i-1][j]
    return F[ns][nt]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return num_distinct_subseq(s, t)

