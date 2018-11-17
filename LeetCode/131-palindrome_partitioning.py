# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp0 = [[]]
        dp1 = []
        for i in range(n):
            for p in dp0:
                assert isinstance(p, list)
                # case 1: just append
                dp1.append(p + [s[i]])
                # case 2: combine with single char
                if len(p) >= 1 and p[-1] == s[i]:
                    dp1.append(p[:-1] + [p[-1] + s[i]])
                # case 3: combine with two palindrome
                if len(p) >= 2 and p[-2] == s[i]:
                    dp1.append(p[:-2] + [p[-2] + p[-1] + s[i]])
            dp0.clear()
            dp0, dp1 = dp1, dp0
        #dp0.sort()
        return dp0
