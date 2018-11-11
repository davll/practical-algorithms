def backtrack(S, i, buffer):
    if i < len(S):
        if S[i].isalpha():
            buffer.append(S[i].lower())
            yield from backtrack(S, i+1, buffer)
            buffer[-1] = S[i].upper()
            yield from backtrack(S, i+1, buffer)
            buffer.pop()
        else:
            buffer.append(S[i])
            yield from backtrack(S, i+1, buffer)
            buffer.pop()
    else:
        yield ''.join(buffer)

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        return list(backtrack(S, 0, []))
