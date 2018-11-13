# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

def inorder(root):
    if not root:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)

def find_2sum(nums, target):
    n = len(nums)
    l, r = 0, n-1
    while l < r:
        tmp = nums[l] + nums[r]
        if tmp == target:
            return True
        elif tmp < target:
            l += 1
        else:
            r -= 1
    return False

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = list(inorder(root))
        return find_2sum(nums, k)
