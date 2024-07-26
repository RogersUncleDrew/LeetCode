class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                curHeight = min(height[left], height[i]) - height[top]
                ans += width * curHeight
            stack.append(i)
        return ans
