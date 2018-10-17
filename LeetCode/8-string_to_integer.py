def atoi(s):
    i, n, val = 0, len(s), 0
    # skip whitespaces
    while i < n and s[i].isspace():
        i += 1
    if i == n:
        return 0
    # detect neg
    neg = (s[i] == '-')
    if s[i] == '-' or s[i] == '+':
        i += 1
    # compute integer
    while i < n and s[i].isdigit():
        val = val * 10 + int(s[i])
        i += 1
    if neg:
        val = -val
    return max(min((2**31)-1, val), -(2**31))

class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        return atoi(s)
