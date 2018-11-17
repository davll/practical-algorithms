# https://leetcode.com/problems/word-ladder-ii/

from collections import deque, defaultdict

def bfs(begin, end, words):
    words = set(words)
    costs = defaultdict(lambda: float('inf'))
    prevs = defaultdict(lambda: [])
    #
    queue = deque([(begin, 1)])
    while queue:
        word, dist = queue.popleft()
        for w in filter(lambda x: x in words, guess(word)):
            d = dist + 1
            if d < costs[w]:
                costs[w] = d
                prevs[w] = set([word])
                queue.append((w, d))
            elif d == costs[w] and word not in prevs[w]:
                prevs[w].add(word)
    #
    def backtrack(word, buffer):
        buffer.append(word)
        if word == begin:
            path = buffer[:]
            path.reverse()
            yield path
        else:
            for w in prevs[word]:
                yield from backtrack(w, buffer)
        buffer.pop()
    return list(backtrack(end, []))

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def guess(word):
    n = len(word)
    for i in range(n):
        k = ord(word[i]) - ord('a')
        for j in filter(lambda x: x != k, range(26)):
            yield word[:i] + LETTERS[j] + word[i+1:]

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        return bfs(beginWord, endWord, wordList)
