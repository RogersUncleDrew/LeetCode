class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        dp = [[[0 for i in range(n)] for j in range(m)] for p in range(k)]
        pre = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                pre[i][j] = pre[i + 1][j] + pre[i][j + 1] - pre[i + 1][j + 1] + (1 if pizza[i][j] == "A" else 0)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[0][i][j] = 1 if pre[i][j] > 0 else 0
                for p in range(1, k):
                    for heng in range(i + 1, m):
                        if pre[i][j] - pre[heng][j] > 0:
                            dp[p][i][j] += (dp[p - 1][heng][j])%mod
                    for shu in range(j + 1, n):
                        if pre[i][j] - pre[i][shu] > 0:
                            dp[p][i][j] += (dp[p - 1][i][shu])%mod
        return dp[k - 1][0][0] % mod
