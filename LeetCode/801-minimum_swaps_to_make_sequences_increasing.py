class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        assert len(A) == len(B)
        n = len(A)
        dp0 = [n+1] * (n)
        dp1 = [n+1] * (n)
        dp0[0] = 0 # no swap => A'[0] = A[0], B'[0] = B[0]
        dp1[0] = 1 # swap    => A'[0] = B[0], B'[0] = A[0]
        for i in range(1, n):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                dp0[i] = min(dp0[i], dp0[i-1] + 0)
            if B[i-1] < A[i] and A[i-1] < B[i]:
                dp0[i] = min(dp0[i], dp1[i-1] + 0)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                dp1[i] = min(dp1[i], dp0[i-1] + 1)
            if B[i-1] < B[i] and A[i-1] < A[i]:
                dp1[i] = min(dp1[i], dp1[i-1] + 1)
        return min(dp0[n-1], dp1[n-1])

# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
