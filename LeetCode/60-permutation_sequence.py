# https://leetcode.com/problems/permutation-sequence/

from itertools import permutations

def kth_perm_v1(n, k):
    TOTAL_NUM_PERMS = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880][:n]
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9][:n]
    permutations = []
    while digits:
        n -= 1
        digit = digits[(k-1) // TOTAL_NUM_PERMS[n-1]]
        digits.remove(digit)
        permutations.append(str(digit))
        k = k % TOTAL_NUM_PERMS[n-1]
    return ''.join(permutations)


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return kth_perm_v1(n, k)
