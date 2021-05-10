from collections import deque
from typing import Deque, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten_helper(self, root: Optional[TreeNode], q: Deque) -> None:
        if not root:
            return

        q.append(root)

        self.flatten_helper(root.left, q)
        self.flatten_helper(root.right, q)

    def flatten(self, root: TreeNode):
        q = deque()
        self.flatten_helper(root, q)

        root_ = q.popleft() if q else None

        while q:
            root_.right = q.popleft()
            root_.left = None

            root_ = root_.right


class Test(unittest.TestCase):
    def test(self):
        #   INITIAL TREE
        #        5
        #     /     \
        #    3       7
        #   / \     / \
        #  2   4   6   8
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)
        tree.right = TreeNode(7)
        tree.right.right = TreeNode(8)
        tree.right.left = TreeNode(6)

        #   FINAL TREE
        #        5
        #         \
        #          3
        #           \
        #            2
        #             \
        #              4
        #               \
        #                7
        #                 \
        #                  6
        #                   \
        #                    8
        result = [5, 3, 2, 4, 7, 6, 8]

        s = Solution()

        s.flatten(tree)

        for i in result:
            self.assertEqual(tree.val, i)
            tree = tree.right

    def test_edge(self):
        tree = TreeNode(1)

        result = [1]

        s = Solution()

        s.flatten(tree)

        for i in result:
            self.assertEqual(tree.val, i)
            tree = tree.right


if __name__ == "__main__":
    unittest.main()
