"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        index = {}
        head2 = head
        newHead= cur=cur2 = Node(0)
        while head:
            newNode = Node(head.val)
            newHead.next = newNode
            newHead = newHead.next
            index[head] = newNode
            head = head.next

        while head2:
            cur.next.random = index[head2.random] if head2.random in index else None
            cur = cur.next
            head2 = head2.next
        return cur2.next
        
