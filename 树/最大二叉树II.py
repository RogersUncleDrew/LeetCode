# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recur(node):
            if not node:
                return TreeNode(val)
            elif node.val < val:
                newNode = TreeNode(val)
                newNode.left = node
                return newNode
            else:
                node.right = recur(node.right)
                return node
        return recur(root)
