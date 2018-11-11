# https://leetcode.com/problems/interleaving-string/

# Idea: Dynamic Programming
#
# F[k;i,j] = S[:k] is formed by the interleaving of A[:i] and B[:j]
#
# F[0;0,0] = True
# F[1;1,0] = A[0] == S[0]
# F[1;0,1] = B[0] == S[0]
#
# F[k;i,j] = False      if k != i + j
#
# F[k;i,0] = F[k-1;i-1,0] and A[i-1] == S[i-1]
# F[k;0,j] = F[k-1;0,j-1] and B[j-1] == S[j-1]
#
# F[k;i,j] = (F[k-1;i-1,j] and A[i-1] == S[(i+j)-1]) or
#            (F[k-1;i,j-1] and B[j-1] == S[(i+j)-1])
#

def check_interleave(A, B, S):
    na, nb, ns = len(A), len(B), len(S)
    if na == 0:
        return B == S
    elif nb == 0:
        return A == S
    elif ns < na + nb:
        return False
    F = [[False] * (nb+1) for _ in range(na+1)]
    F[0][0] = True
    for i in range(1, na+1):
        F[i][0] = F[i-1][0] and A[i-1] == S[i-1]
    for j in range(1, nb+1):
        F[0][j] = F[0][j-1] and B[j-1] == S[j-1]
    for i in range(1, na+1):
        for j in range(1, nb+1):
            k = i + j
            sa = (F[i-1][j] and A[i-1] == S[k-1])
            sb = (F[i][j-1] and B[j-1] == S[k-1])
            F[i][j] = sa or sb
    return F[na][nb] and (na+nb) == ns

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return check_interleave(s1, s2, s3)
