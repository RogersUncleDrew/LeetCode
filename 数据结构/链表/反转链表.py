# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def dfs(node1, node2):
            if node2:
                node = dfs(node2, node2.next)
                node2.next = node1
                return node
            else:
                return node1
        return dfs(None, head)
