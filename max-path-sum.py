from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.global_max = float("-inf")

    def postOrderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left_sum = max(self.postOrderTraversal(root.left), 0)
        right_sum = max(self.postOrderTraversal(root.right), 0)

        local_sum = left_sum + right_sum + root.val

        self.global_max = max(local_sum, self.global_max)

        return root.val + max(left_sum, right_sum)

    def maxPathSum(self, root: TreeNode) -> int:
        self.postOrderTraversal(root)
        global_max = int(self.global_max)
        self.global_max = float("-inf")
        return global_max


class Test(unittest.TestCase):
    def test(self):
        #   INITIAL TREE
        #       -10
        #     /     \
        #    9       20
        #           / \
        #          7   15
        tree = TreeNode(-10)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.right = TreeNode(7)
        tree.right.left = TreeNode(15)

        s = Solution()

        self.assertEqual(s.maxPathSum(tree), 42)


if __name__ == "__main__":
    unittest.main()
