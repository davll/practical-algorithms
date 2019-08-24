#
#
#

VOWELS = { 'a', 'i', 'u', 'e', 'o' }

class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(filter(lambda c: c not in VOWELS, S))
