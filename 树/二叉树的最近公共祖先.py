# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node:
                if node.val == p.val or node.val == q.val:
                    return node
                left,right  = dfs(node.left), dfs(node.right)
                if left and not right:
                    return left
                elif not left and right:
                    return right
                elif left and right:
                    return node
                else:
                    return None
            return None
        return dfs(root)
