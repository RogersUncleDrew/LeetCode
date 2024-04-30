# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        valueList =[]
        import heapq
        heapq.heapify(valueList)
        while head:
            heapq.heappush(valueList, head.val)
            head= head.next
        dummy = ListNode()
        node = dummy
        while valueList:
            newNode = ListNode(heapq.heappop(valueList))
            node.next = newNode
            node = node.next
        return dummy.next
