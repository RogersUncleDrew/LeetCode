# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def bfs():
            nodeList = deque([root])
            res = []
            while nodeList:
                newList = []
                n = len(nodeList)
                for i in range(n):
                    node = nodeList.popleft()
                    newList.append(node.val)
                    if node.left:nodeList.append(node.left)
                    if node.right:nodeList.append(node.right)
                res.append(newList)
            return res[-1][0]
        return bfs()
