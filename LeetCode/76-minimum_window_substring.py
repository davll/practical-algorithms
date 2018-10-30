# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
# https://leetcode.com/problems/minimum-window-substring/discuss/172339/Accepted-Java-Sliding-Window-O(N)-using-1-HashMap

from collections import deque, Counter

def min_window_v1(text, letters):
    required = Counter(letters)
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

def min_window_v2(text, letters):
    required = Counter(letters)
    missings = len(letters)
    i = 0
    ans = None
    for j, c in enumerate(text, 1):
        # consider a window = text[i:j]
        if required[c] > 0:
            missings -= 1
        required[c] -= 1
        # if all required chars are found
        if missings == 0:
            # drain unnecessary chars to shrink the window
            while i < j and required[text[i]] < 0:
                required[text[i]] += 1
                i += 1
            # update answer
            if not ans or j-i <= (ans[1]-ans[0]):
                ans = (i, j)
    if ans:
        i, j = ans
        return text[i:j]
    else:
        return ""

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return min_window_v2(s, t)
