class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def computeMaxRectangle(nums):
            nums = [0] + nums + [0]
            n = len(nums)
            stack = []
            left = [0 for i in range(n)]
            right = [n - 1 for i in range(n)]
            for i in range(1, n):
                while stack and nums[stack[-1]] >= nums[i]:
                    right[stack[-1]] = i
                    stack.pop()
                if stack:
                    left[i] = stack[-1]
                stack.append(i)
            ans = 0
            for i in range(1, n):
                ans = max(ans, nums[i] * (right[i] - left[i] - 1))
            return ans

        m, n = len(matrix), len(matrix[0])
        pre = [[0 for j in range(n)] for i in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(n):
                if matrix[i-1][j] == "1":
                    pre[i][j] = pre[i-1][j] + 1
            ans = max(ans, computeMaxRectangle(pre[i]))
        return ans
