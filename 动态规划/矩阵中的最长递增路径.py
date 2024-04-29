class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        def dfs(i,j):
            if dp[i][j] > 0:
                return dp[i][j]
            ans = 0
            for (x,y) in [(i+1, j), (i-1, j), (i,j-1), (i, j+1)]:
                if 0<=x<m and 0<=y <n and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, dfs(x,y))
            dp[i][j] = ans + 1
            return dp[i][j]
        ans = 1
        for i in range(m):
            for j in range(n):
                dfs(i, j)
                ans = max(ans, dp[i][j])
        return ans
