from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.depth(root.right) +1, self.depth(root.left) +1)

