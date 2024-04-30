# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.node = head
        def recur(node):
            if node:
                if recur(node.next):
                    if self.node.val == node.val:
                        self.node = self.node.next
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return True
        return recur(head)
            
