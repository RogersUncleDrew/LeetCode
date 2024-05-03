# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(numList):
            if numList:
                maxNum = max(numList)
                index = numList.index(maxNum)
                node = TreeNode(maxNum, recur(numList[:index]), recur(numList[index + 1:]) if index < len(numList) else [])
                return node
            else:
                return None

        return recur(nums)
