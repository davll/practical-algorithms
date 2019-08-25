class Solution:
    def wordPattern(self, pattern: str, text: str) -> bool:
        mappings = dict()
        mapped = set()
        words = list(text.split())
        if len(pattern) != len(words):
            return False
        for a, b in zip(pattern, words):
            if a in mappings:
                x = mappings[a]
                if x != b:
                    return False
            elif b in mapped:
                return False
            else:
                mappings[a] = b
                mapped.add(b)
        return True
