class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [height[i] for i in range(n)]
        right_max = [height[i] for i in range(n)]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2, 0, -1):
            right_max[i] = max(right_max[i+1], height[i])
        return sum(min(right_max[i], left_max[i]) - height[i] for i in range(n))
        
