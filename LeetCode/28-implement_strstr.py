def strstr_naive(text, pat):
    if not pat:
        return 0
    n, p = len(text), len(pat)
    for i in range(n):
        if text[i:p+i] == pat:
            return i
    return -1

def kmp_prefix(pat):
    pass

def strstr_kmp(text, pat):
    pass

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return strstr_naive(haystack, needle)
