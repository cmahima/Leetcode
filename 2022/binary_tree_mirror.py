# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def mirror(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right

        def isMirror(p1,q1):
            if not p1 and not q1:
                return True
            if not q1 or not p1:
                return False
            if q1.val != p1.val:
                return False
            return isMirror(q.left, p.right) and isMirror(q.right, p.left)
        return isMirror(p,q)


