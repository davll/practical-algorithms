# https://leetcode.com/problems/longest-palindromic-substring/
# https://leetcode.com/articles/longest-palindromic-substring/

# Idea: Dynamic Programming
#
# P[i,j] = (if the sub-string s[i:j+1] is a palindrome)
#
# P[i,j] = P[i+1,j-1]               if s[i] = s[j]
#        = True                     if i = j
#        = bool(s[i] == s[j])       if j = i+1
#
def longest_palindrome_v1(text):
    n = len(text)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        dp[i][i+1] = (text[i] == text[i+1])
    for k in range(3,n+1):
        for i in range(n-k+1):
            j = i + k - 1
            dp[i][j] = (text[i] == text[j] and dp[i+1][j-1])
    maxlen = 0
    for i in range(n):
        for j in range(i,n):
            if dp[i][j]:
                maxlen = max(maxlen, j-i+1)
    for i in range(n-maxlen+1):
        j = i + maxlen - 1
        if dp[i][j]:
            return text[i:j+1]
    return None

# Idea: Expand around center
def longest_palindrome_v2(text):
    pass

# Idea: Manacher's Algorithm
def longest_palindrome_v3(text):
    from itertools import chain
    s = '#'.join(chain('^', s, '$')
    n = len(s)
    p = [0] * n
    c, r = 0, 0
    for i in range(1, n-1):
        j = 2 * c - i
        p[i] = min(r-i, p[j]) if r > i else 0
        #while s

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        return longest_palindrome_v1(s)
        
# http://www.cnblogs.com/grandyang/p/4475985.html
