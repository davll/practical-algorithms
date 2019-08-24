TABLE = dict(map(lambda t: (t[1], t[0]+1), enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))

class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for x in s:
            n = n * 26 + TABLE[x]
        return n
