# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)
            return node.val + l2 + r2, max(l1 + r1, l2 + r2, l1 + r2, l2 + r1)
        a, b = dfs(root)
        return max(a, b)
