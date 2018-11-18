# https://leetcode.com/problems/repeated-string-match/

# 
def compare_repeated_v1(A, B):
    m, n = len(A), len(B)
    q = (n + m - 1) // m
    if B in A * q:
        return q
    elif B in A * (q+1):
        return (q+1)
    else:
        return -1

# Idea: Rabin-Karp + Rolling Hash
def compare_repeated_v2(A, B):
    m, n = len(A), len(B)
    def check(i):
        return all(A[(i+j)%m] == B[j] for j in range(n))
    hb = sum(map(lambda i: ord(B[i]), range(n)))
    ha = sum(map(lambda i: ord(A[i%m]), range(n)))
    if ha == hb and check(0):
        return (n + m - 1) // m
    for i in range(1,m):
        ha = ha - ord(A[i-1]) + ord(A[(i+n-1)%m])
        if ha == hb and check(i):
            return (i + n + m - 1) // m
    return -1

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        return compare_repeated_v2(A, B)
