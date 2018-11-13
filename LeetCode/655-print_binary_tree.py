# https://leetcode.com/problems/print-binary-tree/

from collections import deque, namedtuple

#    1
#  2   3
# 4 5 6 7
# ...
# (2**lv) .. (2**(lv+1)-1)

Entry = namedtuple('Entry', ['node', 'level', 'index'])

def print_tree(root):
    w, h = find_dimension(root)
    result = [[""] * w for _ in range(h)]
    print_subtree(root, 0, 0, w, result)
    return result

def find_dimension(root):
    if not root:
        return (0, 0)
    lw, lh = find_dimension(root.left)
    rw, rh = find_dimension(root.right)
    dw = max(lw, rw)
    dh = max(lh, rh)
    return (dw * 2 + 1, dh + 1)

def print_subtree(root, y, x, w, result):
    if not root:
        return
    assert w % 2 == 1
    dw = (w - 1) // 2
    m = x + dw
    result[y][m] = str(root.val)
    print_subtree(root.left, y+1, x, dw, result)
    print_subtree(root.right, y+1, m+1, dw, result)

class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        return print_tree(root)
