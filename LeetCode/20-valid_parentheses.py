MAPPING = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def check_parentheses(s):
    stk = []
    for c in s:
        if c in MAPPING:
            stk.append(MAPPING[c])
        else:
            if not stk or stk[-1] != c:
                return False
            stk.pop()
    return len(stk) == 0

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return check_parentheses(s)
