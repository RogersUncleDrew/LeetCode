# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -float("inf")
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.max = max(self.max, left + node.val+right, left+node.val, right+node.val, node.val)
            return max(left + node.val, right+node.val, node.val)
        dfs(root)
        return self.max
