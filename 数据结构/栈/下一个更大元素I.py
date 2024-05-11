class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for n in reversed(nums2):
            while stack and stack[-1]<=n:
                stack.pop()
            res[n] = stack[-1] if stack else -1
            stack.append(n)
        return [res[n] for n in nums1]
