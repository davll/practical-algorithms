from collections import Counter

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        n = len(A)
        diffcount = 0
        for i in range(n):
            if A[i] != B[i]:
                diffcount += 1
        if diffcount == 0:
            wc = Counter(A)
            return any(map(lambda c: c > 1, wc.values()))
        elif diffcount != 2:
            return False
        i, j = 0, n-1
        while i < n:
            if A[i] != B[i]:
                break
            i += 1
        while j >= 0:
            if A[j] != B[j]:
                break
            j -= 1
        return A[i] == B[j] and A[j] == B[i]
