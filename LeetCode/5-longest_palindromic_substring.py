# https://leetcode.com/problems/longest-palindromic-substring/
# https://leetcode.com/articles/longest-palindromic-substring/

# Idea: Dynamic Programming
#
# P[i,j] = (if the sub-string s[i:j+1] is a palindrome)
#
def longest_palindrome_v1(text):
    n = len(text)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        dp[i][i+1] = (text[i] == text[i+1])
    for k in range(3,n):
        for i in range(n):
            ###

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
# http://www.cnblogs.com/grandyang/p/4475985.html
