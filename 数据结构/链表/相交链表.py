# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p,q = headA, headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p if p else None
            
