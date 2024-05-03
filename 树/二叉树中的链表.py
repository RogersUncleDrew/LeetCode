# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def recur(h,r):
            if not h:
                return True
            if not r:
                return False
            return h.val == r.val and (recur(h.next,  r.left) or recur(h.next, r.right))
        if not head:
            return True
        if not root:
            return False
        if recur(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
