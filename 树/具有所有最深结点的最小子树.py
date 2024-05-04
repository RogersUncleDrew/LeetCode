# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depth = 0
        self.ans = None
        def dfs(node, depth):
            if not node:
                self.depth = max(self.depth, depth)
                return depth
            left_depth = dfs(node.left,depth+1)
            right_depth = dfs(node.right, depth+1)
            if left_depth == right_depth == self.depth:
                self.ans = node
            return max(left_depth, right_depth)
        dfs(root, 0)
        return self.ans
