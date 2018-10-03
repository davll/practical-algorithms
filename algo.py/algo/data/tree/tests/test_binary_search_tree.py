from unittest import TestCase
from ..binary_search_tree import BinarySearchTree, Node

def bst1():
    root = Node(20, 'A')
    root.left = Node(5, 'B')
    root.left.left = Node(1, 'C')
    root.left.right = Node(10, 'D')
    root.right = Node(40, 'E')
    root.right.right = Node(100, 'F')
    return BinarySearchTree(root)

class TestBST(TestCase):
    def test_1(self):
        bst = bst1()
        self.assertIn(20, bst)
        self.assertNotIn(1001, bst)
        self.assertIn(1, bst)
        self.assertIn(100, bst)
    def test_inorder(self):
        bst = bst1()
        keys = list(map(lambda x: x[0], bst.inorder()))
        values = list(map(lambda x: x[1], bst.inorder()))
        self.assertListEqual(keys, [1, 5, 10, 20, 40, 100])
        self.assertListEqual(values, ['C', 'B', 'D', 'A', 'E', 'F'])
    def test_preorder(self):
        bst = bst1()
        keys = list(map(lambda x: x[0], bst.preorder()))
        self.assertListEqual(keys, [20, 5, 1, 10, 40, 100])
    def test_postorder(self):
        bst = bst1()
        keys = list(map(lambda x: x[0], bst.postorder()))
        self.assertListEqual(keys, [1, 10, 5, 100, 40, 20])
    def test_levelorder(self):
        bst = bst1()
        keys = list(map(lambda x: x[0], bst.levelorder()))
        self.assertListEqual(keys, [20, 5, 40, 1, 10, 100])
