# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        stack, ptr = [], root

        while stack or ptr:
            if ptr:
                arr.append(ptr.val)
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack.pop()
                ptr = ptr.right

        return arr





