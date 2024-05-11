class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        n = len(nums)
        stack = []
        ans = []
        for num in reversed(nums):
            while stack and stack[-1]<=num:
                stack.pop()
            ans.append(stack[-1] if stack else -1)
            stack.append(num)
        ans = list(reversed(ans))
        return ans[0:n//2]
