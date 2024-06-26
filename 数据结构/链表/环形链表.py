# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p,q = head, head.next
        while p and q and q.next:
            if p==q:
                return True
            p = p.next
            q = q.next.next

        return False
