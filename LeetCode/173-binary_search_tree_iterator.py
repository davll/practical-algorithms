# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.curr = root
        self.stack = []
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.curr:
            while self.curr.left:
                self.stack.append(self.curr)
                self.curr = self.curr.left
        elif self.stack:
            self.curr = self.stack.pop()
        else:
            raise StopIteration()
        val = self.curr.val
        if self.curr.right:
            self.curr = self.curr.right
        else:
            self.curr = None
        return val
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.curr or self.stack)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
