class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        maxL = max(m, n)
        dp = [[False for j in range(m + 1)] for i in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == "*":
                dp[i][0] = True
            else:
                break
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]
                elif p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[i - 1] == s[j - 1]
        return dp[n][m]
