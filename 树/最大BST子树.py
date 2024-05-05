# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth = 0
        def dfs(node):
            if not node:
                return True, 0, float("inf"), -float("inf")
            isLeft, nodeLeft, lmin, lmax = dfs(node.left)
            isRight, nodeRight, rmin, rmax = dfs(node.right)
            size = nodeLeft + nodeRight + 1
            curMin = min(lmin, node.val, rmin)
            curMax = max(rmax, node.val, rmax)
            if isLeft and isRight and lmax<node.val<rmin:
                self.ans = max(self.ans, size)
                return True, size, curMin, curMax
            return False, size, curMin, curMax
        dfs(root)
        return self.ans
