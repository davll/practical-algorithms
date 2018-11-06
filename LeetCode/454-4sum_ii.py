from collections import Counter

# Idea: Hashing
def four_sum_count_v1(A, B, C, D):
    ab = Counter(a+b for a in A for b in B)
    return sum(ab[-c-d] for c in C for d in D)

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        return four_sum_count_v1(A, B, C, D)
