# https://leetcode.com/problems/word-ladder/

from collections import deque

def bfs(begin, end, words):
    words = set(words)
    queue = deque([(begin, 1)])
    while queue:
        word, dist = queue.popleft()
        if word == end:
            return dist
        for w in guess(word):
            if w in words:
                words.remove(w)
                queue.append((w, dist+1))
    return 0

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def guess(word):
    n = len(word)
    for i in range(n):
        k = ord(word[i]) - ord('a')
        for j in filter(lambda x: x != k, range(26)):
            yield word[:i] + LETTERS[j] + word[i+1:]

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        return bfs(beginWord, endWord, wordList)
