# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(root):
            if not root:
                return [True, -1]

            left = balance(root.left)
            right = balance(root.right)

            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [isBalanced, max(left[1], right[1]) + 1]

        return balance(root)[0]