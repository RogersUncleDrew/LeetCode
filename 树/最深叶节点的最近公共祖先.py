# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depthList = defaultdict(list)
        maxDepth = 0
        def dfs(node, depth):
            nonlocal maxDepth
            if not node:
                return
            depthList[depth].append(node)
            maxDepth = max(maxDepth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            return
        dfs(root, 0)
        maxDepthNodelist = depthList[maxDepth]
        n = len(maxDepthNodelist)
        if n == 1:
            return maxDepthNodelist[0]
        ans= None
        def dfs2(node):
            if not node:
                return False,0
            nonlocal ans
            returnV = False
            count=0
            if node in maxDepthNodelist:
                returnV = True
                count+=1
            l1, l2 = dfs2(node.left)
            r1, r2 = dfs2(node.right)
            if l1 : returnV = True
            if r1 : returnV = True
            count+=l2
            count+=r2
            if count >= n:
                ans = node
                return False, 0
            return returnV, count
        dfs2(root)
        return ans
