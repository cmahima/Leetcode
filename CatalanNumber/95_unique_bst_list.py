# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]
        mem = {}
        def dfs(left, right):
            if left>right: return [None]
            if (left, right) in mem:
                return mem[(left,right)]
            ans = []
            for root in range(left, right+1):
                left_tree = dfs(left, root-1)
                right_tree = dfs(root+1, right)
                for l in left_tree:
                    for r in right_tree:
                        node = TreeNode(root, l, r)
                        ans.append(node)
                        mem[(left, right)] = ans
            return ans
        return dfs(1, n)


                