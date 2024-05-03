# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, row,flag):
            if row == depth:
                newNode = TreeNode(val)
                if flag:
                    newNode.left = node
                else:
                    newNode.right = node
                return newNode
            else:
                if node:
                    node.left = dfs(node.left, row+1, True)
                    node.right = dfs(node.right, row+1, False)
                return node
        return dfs(root, 1, True)
