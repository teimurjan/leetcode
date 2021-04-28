import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBSTHelper(self, root: TreeNode, min=float('-inf'), max=float('inf')) -> bool:
        if not root:
            return True
        if root.val > max or root.val < min:
            return False
        if root.left and root.left.val > root.val:
            return False
        if root.right and root.right.val < root.val:
            return False

        return self.isValidBSTHelper(root.left, min, root.val) and self.isValidBSTHelper(root.right, root.val, max)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root)


class Test(unittest.TestCase):
    def test(self):
        #    VALID TREE
        #        5
        #     /     \
        #    3       7
        #   / \     / \
        #  2   4   6   8
        valid_tree = TreeNode(5)
        valid_tree.left = TreeNode(3)
        valid_tree.left.left = TreeNode(2)
        valid_tree.left.right = TreeNode(4)
        valid_tree.right = TreeNode(7)
        valid_tree.right.right = TreeNode(8)
        valid_tree.right.left = TreeNode(6)

        #   INVALID TREE
        #        5
        #     /     \
        #    3       6
        #   / \     / \
        #  2   4   1   7
        invalid_tree = TreeNode(5)
        invalid_tree.left = TreeNode(3)
        invalid_tree.left.left = TreeNode(2)
        invalid_tree.left.right = TreeNode(4)
        invalid_tree.right = TreeNode(6)
        invalid_tree.right.right = TreeNode(7)
        invalid_tree.right.left = TreeNode(1)

        s = Solution()

        self.assertEqual(s.isValidBST(valid_tree), True)
        self.assertEqual(s.isValidBST(invalid_tree), False)


if __name__ == '__main__':
    unittest.main()
