# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
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
            n = len(res)
            return [max(res[i]) for i in range(n)]
        return bfs()
