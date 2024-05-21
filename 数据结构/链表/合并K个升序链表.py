# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        h = [node for node in lists if node]
        heapq.heapify(h)
        curNode = dummy
        while h:
            popNode = heapq.heappop(h)
            curNode.next = popNode
            curNode = curNode.next
            if popNode.next:
                heapq.heappush(h, popNode.next)
        return dummy.next

        
