# https://leetcode.com/problems/restore-ip-addresses/

def backtrack(s: str, i: int, k: int, buffer):
    n = len(s)
    if k < 4 and i < n:
        buffer.append(s[i])
        yield from backtrack(s, i+1, k+1, buffer)
        buffer.pop()
        if s[i] == '0':
            return
        if i < n-1:
            buffer.append(s[i:i+2])
            yield from backtrack(s, i+2, k+1, buffer)
            buffer.pop()
        if i < n-2 and int(s[i:i+3]) <= 255:
            buffer.append(s[i:i+3])
            yield from backtrack(s, i+3, k+1, buffer)
            buffer.pop()
    elif i == n and k == 4:
        yield '.'.join(buffer)

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return list(backtrack(s, 0, 0, []))
