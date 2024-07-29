# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr = []
        stack, ptr, prev = [], root, None

        while stack or ptr:

            if ptr:
                stack.append(ptr)
                ptr = ptr.left

            else:
                top = stack[-1]
                if top.right and top.right != prev:
                    ptr = top.right
                else:
                    arr.append(top.val)
                    prev = top
                    stack.pop()
        return arr