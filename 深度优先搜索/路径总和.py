# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        def dfs(preSum, node):
            if not node:
                return 0
            preSum += node.val
            
            res = 0
            res += prefix[preSum - targetSum]
            prefix[preSum] += 1
            res += dfs(preSum, node.left)
            res += dfs(preSum, node.right)
            prefix[preSum] -= 1
            return res
        return dfs(0, root)
