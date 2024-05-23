class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]
        @cache
        def dfs(n):
            if n == 0 or n==1:
                return 1
            ans = 0
            for j in range(n):
                ans += dfs(j) * dfs(n - j - 1)
            return ans
        return dfs(n)
