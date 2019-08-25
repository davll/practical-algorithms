#
#
#

def numways_v1(n, k):
    if n == 0 or k == 0:
        return 0
    if n == 1:
        return k
    F1, F2 = [[[1] * k for _ in range(k)] for _ in range(2)]
    for _ in range(2,n):
        for k1 in range(k):
            for k2 in range(k):
                if k1 == k2:
                    F2[k1][k2] = sum(F1[k2][k3] for k3 in range(k) if k3 != k2)
                else:
                    F2[k1][k2] = sum(F1[k2][k3] for k3 in range(k))
        F1, F2 = F2, F1
    return sum(sum(F1[i]) for i in range(k))

def numways_v2(n, k):
    if n == 0 or k == 0:
        return 0
    if n == 1:
        return k
    fsame, fdiff = 1, 1
    for _ in range(2, n):
        s = (k-1) * fdiff
        d = fsame + (k-1) * fdiff
        fsame, fdiff = s, d
    return k * fsame + k * (k-1) * fdiff

class Solution:
    def numWays(self, n: int, k: int) -> int:
        return numways_v2(n, k)
