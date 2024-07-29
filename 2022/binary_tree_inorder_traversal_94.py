# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inList = []
        ptr, stack = root, []

        while stack or ptr:
            if ptr:
                stack.append(ptr)
                ptr= ptr.left

            else:
                ptr = stack.pop()
                inList.append(ptr.val)
                ptr = ptr.right

        return inList





