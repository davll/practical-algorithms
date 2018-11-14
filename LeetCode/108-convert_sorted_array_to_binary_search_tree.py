# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def construct(nums):
    if not nums:
        return None
    m = (len(nums)-1) // 2
    root = TreeNode(nums[m])
    root.left = construct(nums[:m])
    root.right = construct(nums[m+1:])
    return root

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return construct(nums)
