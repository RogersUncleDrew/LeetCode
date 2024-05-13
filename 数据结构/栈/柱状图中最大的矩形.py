class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        pre = [0]
        for i in heights:
            pre.append(pre[-1] + i)
        n = len(heights)
        left = [0 for i in range(n)]
        right = [n - 1 for i in range(n)]
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        ans = 0
        for i in range(1, n - 1):
            ans = max((right[i] - left[i] - 1) * heights[i], ans)
        return ans
