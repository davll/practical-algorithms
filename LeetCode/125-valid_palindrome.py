class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        l, r = 0, n-1
        while l < r:
            while l < n and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l >= r:
                break
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
