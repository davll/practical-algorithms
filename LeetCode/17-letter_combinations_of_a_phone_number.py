NUM_TO_LETTERS = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

def backtrack(digits, i, buffer):
    if i < len(digits):
        for c in NUM_TO_LETTERS[digits[i]]:
            buffer[i] = c
            for s in backtrack(digits, i+1, buffer):
                yield s
    else:
        yield ''.join(buffer)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        return list(backtrack(digits, 0, ['0'] * len(digits)))
