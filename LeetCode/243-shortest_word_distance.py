class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = [], []
        for i, w in enumerate(words):
            if word1 == w:
                p1.append(i)
            if word2 == w:
                p2.append(i)
        result = float('inf')
        for a in p1:
            for b in p2:
                result = min(result, abs(a - b))
        return result
