# String Searching

from typing import Iterator

# Knuth Morris Pratt
class KmpSearch:
    def __init__(self, pattern: str) -> None:
        # compute prefix table
        #
        # Define a function F(i) = table[i]
        #     so that S[i-F(i) : i] = S[0 : F(i)]
        #   where F(i) < i
        #         S = pattern string
        #
        # F(i) = 0 where F(i) does not exist
        # F(1) = 0 due to only one character
        #
        table = [0] * (len(pattern) + 1)
        k = 0
        for i in range(1, len(pattern)):
            while k > 0 and pattern[k] != pattern[i]:
                k = table[k]
            if pattern[k] == pattern[i]:
                k += 1
            table[i+1] = k
        # assign attributes
        self.pattern = pattern
        self.table = table
    #
    def search(self, text: str) -> Iterator[int]:
        if not self.pattern:
            yield 0
            return
        # scan the text to feed the state machine
        # k is the current state number starting from 0
        k = 0
        for i, c in enumerate(text):
            # go back if characters mismatch
            while k > 0 and self.pattern[k] != c:
                k = self.table[k]
            # advance if characters match
            if self.pattern[k] == c:
                k += 1
            # have found a match
            if k == len(self.pattern):
                yield (i-k+1)
                # find the next match
                k = self.table[k]

# Boyer Moore

# Rabin Karp
def rabin_karp(text, pattern):
    n, m = map(len, (text, pattern))
    hp = hash(pattern)
    for i in range(n-m+1):
        s = text[i:i+m]
        if hash(s) == hp and s == pattern:
            yield i
