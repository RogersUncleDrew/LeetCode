# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p,q,x = head, head.next, head.next
        while p and p.next and q and q.next:
            
            p.next = p.next.next
            p = p.next
            q.next = q.next.next
            q = q.next
        p.next = x
        return head
