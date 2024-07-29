class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 ==0 or n==0:
            return []
        return self.generate_tree(1, n)
    @cache
    def generate_tree(self,left, right):
        if left > right:
            return [None]

        #if (left,right) in mem: return mem[(left,right)]
        result = []
        for root in range(left, right+1):
            left_tree = self.generate_tree(left, root-1)
            right_tree = self.generate_tree( root+1, right)

            for l in left_tree:
                for r in right_tree:
                    if l==r==None:
                        node = TreeNode(0, l, r)
                        result.append(node)
                        #mem[(left,right)] = result
                    elif (l != None) and (r != None):
                        node = TreeNode(0, l, r)
                        result.append(node)
                        #mem[(left,right)] = result
        return result
        