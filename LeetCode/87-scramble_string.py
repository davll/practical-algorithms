# https://leetcode.com/problems/scramble-string/

def is_scramble(s1, s2):
    assert len(s1) == len(s2)
    if not s1:
        return True
    if len(s1) == 1:
        return s1 == s2
    if len(s1) == 2:
        return s1 == s2 or (s1[0] == s2[1] and s1[1] == s2[0])
    k = len(s1) // 2
    a, b = s1[:k], s1[k:]
    # case1: not swapped


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return is_scramble(s1, s2)
