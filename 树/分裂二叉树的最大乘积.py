# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        index = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            index[node] = node.val + dfs(node.left) + dfs(node.right)
            return index[node]
        dfs(root)
        self.maxV = 0
        totalLength = index[root]
        for i in index:
            self.maxV = max(self.maxV, (totalLength-index[i])*index[i])
        return self.maxV % (10**9 + 7)
