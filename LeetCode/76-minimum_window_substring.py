from collections import deque, Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        text = s
        required = Counter(t)
        count = Counter()
        positions = {}
        queue = deque()
        ans = None
        for i, c in enumerate(text):
            if c in required:
                positions[c] = i
                count[c] += 1
            while queue:
                x = queue[0]
                if x < positions[text[x]] and count[text[x]] > required[text[x]]:
                    queue.popleft()
                    count[text[x]] -= 1
                else:
                    break
            if c in required:
                queue.append(i)
            if all(map(lambda k: count[k] >= required[k], required.keys())):
                if not ans or (queue[-1]-queue[0]) < (ans[1]-ans[0]):
                    ans = (queue[0], queue[-1])
        if ans:
            return text[ans[0]:ans[1]+1]
        else:
            return ""
