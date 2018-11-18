# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s.strip().split())
        result.reverse()
        return ' '.join(result)
