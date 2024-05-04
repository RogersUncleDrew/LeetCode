# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def computeDepth(node):
            if not node:
                return 0
            else:
                return max(computeDepth(node.left), computeDepth(node.right)) + 1
        depth = computeDepth(root)
        length = 2**depth -1
        res = [[""] * length for _ in range(depth)]
        def dfs(node, d, p):
            if not node:
                return
            res[d][p] = str(node.val)
            dfs(node.left, d+1, p - 2**(depth - d - 2))
            dfs(node.right, d+1, p + 2**(depth - d - 2))
        dfs(root, 0, (length - 1)//2)
        return res
