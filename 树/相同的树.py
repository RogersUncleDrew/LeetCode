# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recur(n1, n2):
            if n1 and n2:
                return n1.val == n2.val and recur(n1.left, n2.left) and recur(n1.right, n2.right)
            elif n1 is None and n2 is None:
                return True
            else:
                return False
        return recur(p,q)
