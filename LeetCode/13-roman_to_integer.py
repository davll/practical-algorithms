SYMBOLS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman2int(roman):
    result = 0
    prev = None
    for c in reversed(roman):
        if prev and SYMBOLS[prev] > SYMBOLS[c]:
            result -= SYMBOLS[c]
        else:
            result += SYMBOLS[c]
        prev = c
    return result

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return roman2int(s)
