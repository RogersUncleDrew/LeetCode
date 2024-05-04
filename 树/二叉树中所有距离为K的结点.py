# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        childrenList = defaultdict(list)
        def dfs(node, parent):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                childrenList[node] = [parent, node.left, node.right]
        dfs(root, None)
        ans = []
        def dfs2(node, parent, depth):
            if node:
                if depth == k:
                    ans.append(node.val)
                elif depth > k:
                    return
                for child in childrenList[node]:
                    if child!=parent:
                        dfs2(child, node, depth+1)
        dfs2(target, None, 0)
        return ans
