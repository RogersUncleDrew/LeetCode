# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recur_isSame(p,q):
            if not p and not q:
                return True
            elif p and q:
                return p.val ==q.val and recur_isSame(p.left, q.left) and recur_isSame(p.right, q.right)
            else:
                return False
        def recur_isSub(p,q):
            if not p and not q:
                return True
            elif p and q:
                return recur_isSame(p,q) or recur_isSub(p.left, q) or recur_isSub(p.right, q)
            else:
                return False
        return recur_isSub(root, subRoot)
