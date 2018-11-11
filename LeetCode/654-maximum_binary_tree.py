def build(nums):
    if not nums:
        return None
    i, v = max(enumerate(nums), key=lambda t: t[1])
    root = TreeNode(v)
    root.left = build(nums[:i])
    root.right = build(nums[i+1:])
    return root

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return build(nums)
